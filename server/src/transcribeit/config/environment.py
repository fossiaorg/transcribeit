import os
from typing import List
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from ..helpers.singleton import singleton


load_dotenv()


@singleton
class EnvVarConfig(BaseSettings):
    environment: str
    cookie_domain: str
    api_domain: str
    frontend_url: str
    uploads_dir: str
    pyannote_metrics_enabled: str = "0"
    hf_pyannote_model: str = "pyannote/speaker-diarization-community-1"
    hf_pyannote_access_token: str

    class EnvVarConfig:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_env_config():
    return EnvVarConfig()
