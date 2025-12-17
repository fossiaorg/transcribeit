import os
import logging
from pathlib import Path
from .environment import EnvVarConfig
from ..helpers.singleton import singleton
from faster_whisper import WhisperModel


@singleton
class AppConfig:
    def __init__(self):
        self.env: EnvVarConfig = EnvVarConfig()
        self.whisper_model = WhisperModel("small", device="cpu")
        self.ensure_upload_directory()

    def ensure_upload_directory(self):
        upload_dir = Path(self.env.uploads_dir)
        if not upload_dir.exists():
            try:
                upload_dir.mkdir(parents=True, exist_ok=True)
                logging.info(f"Upload directory created: {upload_dir}")
            except PermissionError:
                logging.error(
                    f"Permission error: Unable to create directory {upload_dir}."
                )
                raise
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                raise
        else:
            logging.info(f"Upload directory already exists: {upload_dir}")

        if not os.access(upload_dir, os.W_OK):
            logging.error(
                f"Permission error: No write access to directory {upload_dir}."
            )
            raise PermissionError(f"Cannot write to directory {upload_dir}.")
        else:
            logging.info(f"Upload directory instantiated: {upload_dir}")


def get_config() -> AppConfig:
    return AppConfig()
