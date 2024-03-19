import struct
import asyncio
import serial

from loguru import logger

from reactivex.subject import Subject
from ..tools.speex_decoder import speex_decoder


class DataHead:
    HEAD_MAGIC = 0
    HEAD_CHECKSUM = 1
    HEAD_TYPE = 2
    HEAD_LEN = 3
    HEAD_VERSION = 4
    HEAD_FILL_DATA = 5


class FillCode:
    DEF_FILL = 0x12345678
    INVAILD_SPEAK = 0x12345666
    TTS_FILL = 0x12345677
    MP3_FILL = 0x12345688
    M4A_FILL = 0x123456aa
    REPEAT_FILL = 0x123456ab
    WAV_FILL = 0x123456bb
    NO_WAKE_FILL = 0x0


class TypeCode:
    DEVICE_SLEEP = 0x0000
    LOCAL_ASR_NOTIFY = 0x0101
    WAKE_UP = 0x0102
    VAD_END = 0x0103
    SKIP_INVAILD_SPEAK = 0x0104
    PCM_MIDDLE = 0x0105
    PCM_FINISH = 0x0106
    PCM_IDLE = 0x0107
    NET_PLAY_START = 0x0201
    NET_PLAY_PAUSE = 0x0202
    NET_PLAY_RESUME = 0x0203
    NET_PLAY_STOP = 0x0204
    NET_PLAY_RESTART = 0x0205
    NET_PLAY_NEXT = 0x0206
    NET_PLAY_LOCAL_TTS = 0x0207
    NET_PLAY_END = 0x0208
    NET_PLAY_RECONECT_URL = 0x0209
    PLAY_DATA_GET = 0x020a
    PLAY_DATA_RECV = 0x020b
    PLAY_DATA_END = 0x020c
    PLAY_TTS_END = 0x020d
    PLAY_EMPTY = 0x020e
    PLAY_NEXT = 0x020f
    PLAYING_TTS = 0x0210
    PLAY_RESUME_ERRO = 0x0211
    PLAY_LAST = 0x0212
    QCLOUD_IOT_CMD = 0x0301
    NET_VOLUME = 0x0302
    LOCAL_VOLUME = 0x0303
    VOLUME_INC = 0x0304
    VOLUME_DEC = 0x0305
    VOLUME_MAXI = 0x0306
    VOLUME_MINI = 0x0307
    ENTER_NET_CONFIG = 0x0401
    NET_CONFIGING = 0x0402
    EXIT_NET_CONFIG = 0x0403
    INIT_SMARTCONFIG = 0x0404
    WIFI_DISCONNECTED = 0x0405
    WIFI_CONNECTED = 0x0406
    GET_PROFILE = 0x0407
    NEED_PROFILE = 0x0408
    CLOUD_CONNECTED = 0x0409
    CLOUD_DISCONNECTED = 0x040a
    NET_CONFIG_SUCCESS = 0x040b
    NET_CONFIG_FAIL = 0x040c
    CIAS_OTA_START = 0x0501
    CIAS_OTA_DATA = 0x0502
    CIAS_OTA_SUCESS = 0x0503
    CIAS_FACTORY_START = 0x0504
    CIAS_FACTORY_OK = 0x0505
    CIAS_FACTORY_FAIL = 0x0506
    CIAS_FACTORY_SELF_TEST_START = 0x0507
    CIAS_IR_DATA = 0x0508
    CIAS_IR_LOADING_DATA = 0x0509
    CIAS_IR_LOAD_DATA_OVER = 0x050a
    CIAS_IR_LOAD_DATA_START = 0x050b
    CIAS_CJSON_DATA = 0x0601
    SINGLE_CONVERSATION = 0x0701
    MANUAL_CONVERSATION = 0x0702
    MULTI_CONVERSATION = 0x0703


class MediaState:
    MEDIA_IDLE = 0x00
    MEDIA_PCM_SEND = 0x01
    MEDIA_MP3_GET = 0x02
    MEDIA_MP3_CHECK = 0x03
    MEDIA_MP3_PLAY = 0x04
    MEDIA_MP3_PAUSE = 0x05


MEDIA_READ_LENGTH = 1024
STANDARD_HEAD_LEN = 16


class AudioModule:
    event = Subject()

    def __init__(self, port, baud, event):
        self.aigc_event = event
        self.port = port
        self.baud = baud
        self.serial = None
        self.running = True

        self.state = TypeCode.DEVICE_SLEEP
        # self.prev_state = TypeCode.DEVICE_SLEEP
        self.media_state = TypeCode.DEVICE_SLEEP
        self.conversation_mode = TypeCode.MULTI_CONVERSATION

        self.format_string = 'IHHHHI'
        self.read_length = STANDARD_HEAD_LEN
        self.pcm_data = bytearray()
        self.decode_data = bytes()
        self.media_data = bytes()
        self.media_read_start = 0
        self.media_read_end = MEDIA_READ_LENGTH
        self.media_count = 0
        self.cmd_action = {TypeCode.WAKE_UP: self.wakeup,
                           TypeCode.LOCAL_ASR_NOTIFY: self.local,
                           TypeCode.PCM_MIDDLE: self.record,
                           TypeCode.PCM_FINISH: self.upload,
                           TypeCode.PLAY_DATA_GET: self.media,
                           TypeCode.PLAY_DATA_RECV: self.media}
        self.lasted_event = ""

        start_data = 'A5 A5 5A 5A 00 00 01 02 00 00 00 00 77 56 34 12'
        head_data = 'A5 A5 5A 5A 00 00 0A 02 00 00 00 00 77 56 34 12'
        end_data = 'A5 A5 5A 5A 00 00 0C 02 00 00 00 00 77 56 34 12'
        stop_data = 'A5 A5 5A 5A 00 00 0D 02 00 00 00 00 77 56 34 12'
        hex_values = start_data.split()
        self.start_byte_data = bytes.fromhex(''.join(hex_values))
        hex_values = head_data.split()
        self.head_byte_data = bytearray(bytes.fromhex(''.join(hex_values)))
        hex_values = end_data.split()
        self.end_byte_data = bytes.fromhex(''.join(hex_values))
        hex_values = stop_data.split()
        self.stop_byte_data = bytes.fromhex(''.join(hex_values))

        # 订阅aigc发出得事件
        self.aigc_event.subscribe(lambda i: self.event_handler(i))

    def init(self):
        # logger.debug(f'{self.port, self.baud}')
        self.serial = serial.Serial(self.port, self.baud, timeout=2)
        # 初始化对话模式
        hex_length = (self.conversation_mode.bit_length() + 1)
        bytes_obj = self.conversation_mode.to_bytes(hex_length, byteorder='little')

        self.serial.write(bytes_obj)

    def event_handler(self, event):
        if event["type"] == "play":
            # 发起播放开始事件
            # 判断当前播放事件是否已经发起
            self.event.on_next({"type": "on_play_begin", "data": ""})
            self.media_data = event["data"]
            self.state = TypeCode.NET_PLAY_START
            self.write(self.start_byte_data)
            self.media_count = 0
            self.media_read_start = 0
            self.media_read_end = MEDIA_READ_LENGTH
            self.media(event["data"])

    async def run(self):
        logger.info('serial run')
        while True:
            # logger.info('test run1')
            # time.sleep(2)
            # audio_data = self.device.audio_download_queue.get(False)
            # if not self.device.audio_download_queue.empty():
            #     # print('audio download')
            #     self.media_data = self.device.audio_download_queue.get()
            #     # print(self.media_data)
            #     self.write(self.start_byte_data)
            #     # self.media_state = MEDIA_MP3_CHECK
            #     self.media_count = 0
            #     self.media_read_start = 0
            #     self.media_read_end = MEDIA_READ_LENGTH

            data = self.serial.read(self.read_length)
            if len(data) < self.read_length:
                # time.sleep(0.005)
                # if len(data):
                #     print(data)
                pass
            else:
                self.data_parse(data)
                func = self.cmd_action.get(self.state)
                if func:
                    func(data)
                else:
                    # logger.debug(f'>>>>>>>>>>>>>>>>>>>>>{self.state}')
                    hex_string = ' '.join(format(x, '02X') for x in data)
                    logger.debug(f'->{hex_string}')

            await asyncio.sleep(0)

        self.serial.close()
        # await asyncio.sleep(0)

    def data_parse(self, data):
        hex_string = ' '.join(format(x, '02X') for x in data)
        # logger.debug(f'->{hex_string}')

        read_length = len(data)
        if read_length >= STANDARD_HEAD_LEN:
            if self.read_length > STANDARD_HEAD_LEN:
                self.read_length = STANDARD_HEAD_LEN
            else:
                unpacked_data = struct.unpack(self.format_string, data)
                data_length = unpacked_data[DataHead.HEAD_LEN]

                # self.prev_state = self.state
                self.state = unpacked_data[DataHead.HEAD_TYPE]
                if data_length > 0:
                    self.read_length = data_length

    def upload(self, data):
        # self.media_state = MEDIA_PCM_SEND
        # with open('pcm_log_speex_encode.pcm', 'wb') as f:
        #     for i in self.pcm_data:
        #         f.write(bytes([i]))
        # #
        # # url = "http://101.34.93.13:7979/encoded_voice"
        # url = "http://101.34.93.13:7676/decode"
        # filename = 'pcm_log_speex_encode.pcm'
        # # file = open('C:/Users/i3water/PycharmProjects/pythonProject1/PCM_TEST/pcm_log_speex_encode.pcm', 'rb')
        # #
        # # # asyncio.run(speex_decode(url, filename, file))
        # payload = {}
        # files = [
        #     ('file',
        #      ('pcm_log_speex_encode.pcm',
        #       self.pcm_data,
        #       # open('C:/Users/i3water/PycharmProjects/pythonProject1/PCM_TEST/pcm_log_speex_encode.pcm', 'rb'),
        #       'application/octet-stream'))
        # ]
        # headers = {}
        #
        # response = requests.request("POST", url, headers=headers, data=payload, files=files)

        # with open('pcm_log_speex_decode.mp3', 'wb') as f:
        #     f.write(response.content)
        # self.media_data = response.content
        # print(response.text)
        if not len(self.pcm_data):
            logger.info('None pcm data to upload.')
            return

        # 解码音频文件
        # self.decode_data = speex_decoder(self.pcm_data)

        # 发起录音结束事件，并传出录音数据
        # self.event.on_next({"type": "on_record_end", "data": self.decode_data})
        self.event.on_next({"type": "on_record_end", "data": self.pcm_data})
        self.lasted_event = "on_record_end"

        # logger.info('Pcm data to upload.')
        #
        # self.device.audio_upload_queue.put(self.pcm_data)

        # with open('greatest_16k_s16le.mp3', 'rb') as file:
        #     self.media_data = file.read()
        #
        # print('media mp3 get')

        self.pcm_data = bytearray()
        # # self.media_state = MEDIA_MP3_GET
        #
        # self.write(self.start_byte_data)
        # # self.media_state = MEDIA_MP3_CHECK
        # self.media_count = 0
        # self.media_read_start = 0
        # self.media_read_end = MEDIA_READ_LENGTH

    def send_media_data(self):
        send_data = self.media_data[self.media_read_start: self.media_read_end]
        if send_data:
            data_length = len(send_data)
            packed_data = bytearray(struct.pack('<H', data_length))
            self.head_byte_data[8: 10] = packed_data
            send_data = self.head_byte_data + send_data
            self.write(send_data)
            self.media_count += 1
            self.media_read_start += MEDIA_READ_LENGTH
            self.media_read_end += MEDIA_READ_LENGTH
        else:
            self.write(self.end_byte_data)
            self.media_count = 0
            self.media_read_start = 0
            self.media_read_end = MEDIA_READ_LENGTH
            # logger.info('Media data send completed')

            # 发起播放结束事件
            self.event.on_next({"type": "on_play_end", "data": ""})
            self.lasted_event = "on_play_end"

    def media(self, data):
        if self.media_count == 0:
            for i in range(10):
                self.send_media_data()
            return
        else:
            self.send_media_data()

    def wakeup(self, data):
        # logger.info('DEVICE WAKE UP')
        self.event.on_next({"type": "wakeup", "data": data})

    def local(self, data):
        self.pcm_data = bytearray()
        # self.device.audio_upload_cancel = True
        logger.info(f'LOCAL ASR NOTIFY')

        # 发起离线指令识别事件
        self.event.on_next({"type": "on_recognition", "data": data})

    def record(self, data):
        # 发起录音开始事件
        # 判断当前录音事件是否已经发起
        if self.lasted_event != "on_record_begin":
            self.event.on_next({"type": "on_record_begin", "data": ""})
            self.lasted_event = "on_record_begin"

        # self.device.audio_upload_cancel = False
        if len(data) > STANDARD_HEAD_LEN:
            self.pcm_data += bytearray(data)

    def write(self, data):
        # hex_string = ' '.join(format(x, '02X') for x in data)
        # logger.debug(f'<-{hex_string}')
        self.serial.write(data)

    def stop(self):
        self.running = False

    def get_audio(self):
        return self.decode_data

    def set_conversation_mode(self, mode):
        if mode == "single":
            self.conversation_mode = TypeCode.SINGLE_CONVERSATION
        elif mode == "manual":
            self.conversation_mode = TypeCode.MANUAL_CONVERSATION
        elif mode == "multi":
            self.conversation_mode = TypeCode.MULTI_CONVERSATION
        else:
            raise Exception("Invalid conversation mode")
