from src.transcribeit.config import AppConfig, get_config


config: AppConfig = get_config()


def get_speaker_diarization(audio_path: str):
    diarization_results = config.speaker_diarization_pipeline(audio_path)
    diarization_data = []
    for turn, speaker in diarization_results.speaker_diarization:
        diarization_data.append({"speaker": speaker, "start": turn.start, "end": turn.end})
    return diarization_data