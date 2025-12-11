# Contributing

## Project structure

The project is structured as a monorepo with:
- Frontend, written in Next.js, residing in `frontend/` directory.
- Backend, written in FastAPI, residing in `backend/` directory.

## Pre-requisites

Ensure you have the following dependencies installed on your system:
1. Python 3.13 or later: For running the backend
2. uv: Project and dependency management for backend
3. Yarn: Frontend package management
4. Node.js 22 or later
5. pre-commit: Needed for ensuring code consistency
6. Docker and Docker Compose v2: Needed for running the project setup in containerized manner.

## Set up the project

There are 2 ways to run the project:

## Docker Compose

This is the simplest and recommended way to run TranscribeIt for local development and testing.

1. Clone the project
```sh
git clone https://github.com/fossiaorg/transcribeit
cd transcribeit
```

2. Configure environment variables for frontend
```sh
cp .env.sample .env
# Edit the values as per needed for .env
```

3. Configure environment variables for backend
```sh
cp .env.sample .env
# Edit the values as per needed for .env
```

4. In the project root directory, start the Docker Compose cluster with the following command:
```sh
docker compose up --build # Build the images first
```

The frontend should be accessible at http://localhost:3000.
The backend should be accessible at http://localhost:8000.

## Manual

1. Clone the project
```sh
git clone https://github.com/fossiaorg/transcribeit
cd transcribeit
```

2. Set up frontend
```sh
cd frontend
yarn install
```

3. Configure environment variables for frontend
```sh
cp .env.sample .env
# Edit the values as per needed for .env
```

4. Set up backend
```sh
cd backend
uv sync
source .venv/bin/activate
```

5. Configure environment variables for backend
```sh
cp .env.sample .env
# Edit the values as per needed for .env
```

6. Run the frontend and backend
    - For frontend
    ```sh
    yarn dev
    ```
    - For backend
    ```sh
    fastapi dev src/transcribeit/server.py
    ```

The frontend should be accessible at http://localhost:3000.

The backend should be accessible at http://localhost:8000.