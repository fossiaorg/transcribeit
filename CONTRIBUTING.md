# Contributing

## Project structure

The project is structured as a monorepo with:
- Frontend, written in Next.js, residing in `frontend/` directory.
- Backend, written in FastAPI, residing in `backend/` directory.

## Pre-requisites

Ensure you have the following dependencies installed on your system:
1. [Python 3.13 or later](https://www.python.org): For running the backend
2. [uv](https://docs.astral.sh/uv/): Project and dependency management for backend
3. [Yarn](https://yarnpkg.com/): Frontend package management
4. [Node.js 22](https://nodejs.org) or later
5. [pre-commit](https://pre-commit.com/): Needed for ensuring code consistency
6. [Docker](https://docker.com) and [Docker Compose v2](https://docs.docker.com/compose/): Needed for running the project setup in containerized manner.

## Getting started

There are 2 ways to run the project:

### Docker Compose

This is the simplest and recommended way to run TranscribeIt for local development and testing.

1. Clone the fork of your project project
```sh
git clone https://github.com/<your-username>/transcribeit
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

### Manual

1. Clone the project
```sh
git clone https://github.com/<your-username>/transcribeit
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

## Contributing

To contribute code to TranscribeIt:
1. Check if an issue has been created on GitHub at https://github.com/fossiaorg/transcribeit/issues. If you are a beginner, we suggest you to look at issues labelled `good-first-issue`.
2. If an issue exists, request for an assignment by commenting below the issue. If an issue does not exist, create a new issue with the issue scope -- bug or feature.
3. Create a fork after assignment for the issue and clone your fork to the local machine.
``` sh
git clone https://github.com/<your-username>/transcribeit
```
4. Create a new branch with a branch name that describes the purpose of the branch.
    If you're adding a feature, you can use this convention:
    ``` sh
    git checkout -b feat/<your-feature-name>
    ```

    If you're fixing a bug:
    ``` sh
    git checkout -b fix/<your-feature-name>
    ```
5. Install pre-commit hooks by doing the following in your cloned repository's root directory.
    
    For frontend:
    ``` sh
    cd frontend
    pre-commit install
    ```

    For backend:
    ``` sh
    cd backend
    pre-commit install
    ```
6. Make your changes and commit them with a meaningful commit message.
7. Test your changes locally and ensure lints are done by pre-commit.
8. Once the changes are pushed to your fork, make a pull request by navigating to your forked repository on GitHub by selecting your new branch.
9. Make a pull request against `dev` branch. Pull requests (PR) to `main` will not be considered as it will introduce breaking changes. Provide a detailed description for your PR.