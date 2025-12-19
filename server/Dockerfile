FROM python:3.13-slim-bookworm

RUN pip install uv

WORKDIR /backend

RUN mkdir uploads

RUN apt-get update

RUN apt-get install -y build-essential ca-certificates libasound2-dev libssl-dev wget ffmpeg

COPY pyproject.toml uv.lock README.md ./

COPY src/transcribeit/ ./src/transcribeit/

RUN uv sync

RUN uv add gunicorn

EXPOSE 80

EXPOSE 443

EXPOSE 8000

ENTRYPOINT [".venv/bin/python", "-m", "gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker","-b", "0.0.0.0:8000","src.transcribeit.server:app"]