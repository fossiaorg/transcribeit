import os
from ..config import AppConfig, get_config

config: AppConfig = get_config()


def transcribe_audio(audio_path: str):
    segments, info = config.whisper_model.transcribe(audio_path)
    segment_data = []
    for segment in segments:
        segment_data.append(
            {"start": segment.start, "end": segment.end, "text": segment.text}
        )
    os.remove(audio_path)
    return segment_data
