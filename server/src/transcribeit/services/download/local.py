from uuid import uuid4
import aiofiles
from fastapi import UploadFile, File
from ...helpers.filename import get_filename_hash
from ...config import AppConfig, get_config


config: AppConfig = get_config()


async def download_to_fs(file: UploadFile = File(...)):
    temp_name: str = f"{str(uuid4())}"
    file_name: str = file.filename
    output_path: str = f"{config.env.uploads_dir}/{temp_name}-{file_name}"
    async with aiofiles.open(output_path, "wb") as output_file:
        content = await file.read()
        await output_file.write(content)
    return f"{output_path}", error_code
