import logging
import os
from pathlib import Path
import sys
from .environment import EnvVarConfig
from ..helpers.singleton import singleton
from faster_whisper import WhisperModel
from framestoryx.video_describer import VideoDescriber
from pyannote.audio import Pipeline
from framestoryx.video_describer import VideoDescriber
from pyannote.audio import Pipeline

@singleton
class AppConfig:
    def __init__(self):
        self.env: EnvVarConfig = EnvVarConfig()
        self.whisper_model = WhisperModel("small", device="auto")
        self.speaker_diarization_pipeline = Pipeline.from_pretrained(self.env.hf_pyannote_model, token=self.env.hf_pyannote_access_token)
        self.video_describer: VideoDescriber = VideoDescriber(show_progress=False)
        self.whisper_model = WhisperModel("small", device="cpu")
        self.speaker_diarization_pipeline = Pipeline.from_pretrained(self.env.hf_pyannote_model, token=self.env.hf_pyannote_access_token)
        self.video_describer: VideoDescriber = VideoDescriber(show_progress=False)
        self.ensure_upload_directory()

    def ensure_upload_directory(self):
        uploads_dir = self.env.uploads_dir
        if not uploads_dir:
            logging.error("Startup Error: UPLOADS_DIR is not set in environment variables.")
            logging.error("Please set UPLOADS_DIR in your .env file.")
            sys.exit(1)

        if not os.path.isabs(uploads_dir):
            logging.error(f"Startup Error: UPLOADS_DIR must be an absolute path.")
            logging.error(f"Current value: '{uploads_dir}'")
            logging.error("Please update your .env file to use a full path (e.g., /app/downloads or C:\\downloads).")
            sys.exit(1)

        upload_dir = Path(self.env.uploads_dir)
        if not upload_dir.exists():
            try:
                os.makedirs(uploads_dir, exist_ok=True)
                logging.info(f"Upload directory created: {upload_dir}")

            except PermissionError:
                logging.error(
                    f"Permission error: Unable to create directory {upload_dir}."
                )
                sys.exit(1)

            except OSError as e:
                logging.error(f"Startup Error: Could not create UPLOADS_DIR at '{uploads_dir}': {e}")
                sys.exit(1)

            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                sys.exit(1)

        else:
            logging.info(f"Upload directory already exists: {upload_dir}")

        if not os.access(upload_dir, os.W_OK):
            logging.error(
                f"Permission error: No write access to directory {upload_dir}."
            )
            sys.exit(1)
        else:
            logging.info(f"Upload directory instantiated: {upload_dir}")


def get_config() -> AppConfig:
    return AppConfig()
