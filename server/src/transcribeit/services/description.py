from typing import Optional
from src.transcribeit.config import AppConfig, get_config


config: AppConfig = get_config()


def get_video_description(video_path: Optional[str] = None, video_url: Optional[str] = None):
    if not video_path and not video_url:
        raise Exception("Video path and video URL is not provided")
    if video_url:
        descriptions = config.video_describer.get_video_descriptions(video_url=video_url)
    else:
        descriptions = config.video_describer.get_video_descriptions(video_path)
    return descriptions