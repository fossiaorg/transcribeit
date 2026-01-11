import torchaudio
from src.transcribeit.config import AppConfig, get_config


config: AppConfig = get_config()


def get_speaker_diarization(audio_path: str):
    waveform, sample_rate = torchaudio.load(audio_path)
    diarization_results = config.speaker_diarization_pipeline({
        "waveform": waveform,
        "sample_rate": sample_rate
    })
    diarization_data = []
    for turn, speaker in diarization_results.speaker_diarization:
        diarization_data.append({"speaker": speaker, "start": turn.start, "end": turn.end})
    return diarization_data