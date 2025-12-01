from .environment import EnvVarConfig
from ..helpers.singleton import singleton
from faster_whisper import WhisperModel


@singleton
class AppConfig:
    def __init__(self):
        self.env: EnvVarConfig = EnvVarConfig()
        self.whisper_model = WhisperModel("small", device="cpu")

def get_config() -> AppConfig:
    return AppConfig()