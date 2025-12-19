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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.env.frontend_url],
    allow_methods=cors_allowed_methods,
    allow_headers=["*"],
    expose_headers=["*"],
    allow_credentials=True,
)
app.include_router(v1_router, prefix="/api/v1")
