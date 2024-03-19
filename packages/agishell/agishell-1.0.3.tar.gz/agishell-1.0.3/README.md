# agi-shell

## 安装
```
pip install agi-shell
```

## 快速开始
```python
from agi_shell import Shell
from agishell.tools import speech_to_text, text_to_speech, speex_decoder

aigc = AIGC('COM4')
aigc.set_key('openai_key')
aigc.set_server('openai_url')
agic.init()

# 订阅处理
def event_handler(event):
    if event["type"] == "on_record_end":
        print("录音结束")
        wav_data = speex_decoder(event["data"])
        # 调用语音转文字工具,使用的是openai的whisper模型
        text = speech_to_text(wav_data)
        # 调用大模型
        aigc.send_message(text)
    elif event["type"] == "on_invoke_end":
        print("调用结束")
        # 调用文字转语音工具
        speech_data = text_to_speech(event["data"])
        # 调用speex解码
        aigc.play(speech_data)
    else:
        print(event)

aigc.subscribe(event_handler)
aigc.run()
```