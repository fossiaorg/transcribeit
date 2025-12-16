import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from .config import AppConfig
from .constants.middleware import cors_allowed_headers, cors_allowed_methods
from .routers.api.v1 import router as v1_router


logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("server")
app = FastAPI()
config: AppConfig = AppConfig()
uploads_dir = config.env.uploads_dir

if not uploads_dir:
    logger.critical("Startup Error: UPLOADS_DIR is not set in environment variables.")
    logger.critical("Please set UPLOADS_DIR in your .env file.")
    sys.exit(1)

if not os.path.isabs(uploads_dir):
    logger.critical(f"Startup Error: UPLOADS_DIR must be an absolute path.")
    logger.critical(f"Current value: '{uploads_dir}'")
    logger.critical("Please update your .env file to use a full path (e.g., /app/downloads or C:\\downloads).")
    sys.exit(1)

# Ensure the directory exists (Maintainer approved creating it if missing)
try:
    os.makedirs(uploads_dir, exist_ok=True)
except OSError as e:
    logger.critical(f"Startup Error: Could not create UPLOADS_DIR at '{uploads_dir}': {e}")
    sys.exit(1)

logger.info(f"UPLOADS_DIR is valid: {uploads_dir}")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.env.frontend_url],
    allow_methods=cors_allowed_methods,
    allow_headers=["*"],
    expose_headers=["*"],
    allow_credentials=True,
)
app.include_router(v1_router, prefix="/api/v1")
