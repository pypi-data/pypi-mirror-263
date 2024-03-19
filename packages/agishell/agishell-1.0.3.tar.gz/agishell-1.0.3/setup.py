from setuptools import setup, find_packages

setup(
    name="agishell",
    version="1.0.3",
    packages=find_packages(
        where='src',
        include=['*'],
        exclude=['tests']
    ),
    install_requires=[
        "python-dotenv == 1.0.1",
        "reactivex == 4.0.4",
        "tiktoken == 0.6.0",
        "tenacity == 8.2.3",
        "SpeechRecognition",
        "loguru",
        "requests",
        "pyserial",
        "openai"
    ]
)
