# TranscribeIt

TranscribeIt is a free software transcription service for online videos, live streams and local multimedia content.

# Why?

Hard of hearing and speech population, people with visual impairments and sensory processing disorders have difficulty navigating video content. With online platforms providing little to no transcriptions or inaccurate transcriptions, especially for live streams, it hinders acccessibility. TransribeIt aims to provide customized and diarized transcriptions for making video content accessible.

# Features

1. Transcribe videos and livestreams from YouTube and other online sources supported by [yt-dlp](https://pypi.org/project/yt-dlp).
2. Get transcriptions with timestamps in an intuitive UI for multiple languages using [faster-whisper](https://pypi.org/project/faster-whisper)

# Screenshots

![TranscribeIt interface for providing URL and viewing processed transcripts with timestamps](./assets/transcription-screenshot-01.png)

# Roadmap

- Download transcripts in different formats (WebVTT, SRT, JSON, etc.)
- Include speaker diarization
- Background processing
- Transcription from local audio file uploads

# Quickstart

1. Clone the project
```sh
git clone https://github.com/fossiaorg/transcribeit
cd transcribeit
```

2. Set up frontend
```sh
cd web
yarn install
```

3. Configure environment variables for frontend
```sh
cp .env.sample .env
# Edit the values as per needed for .env
```

4. Set up backend
```sh
cd server
uv sync
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
    source .venv/bin/activate
    fastapi dev src/transcribeit/server.py
    ```

The frontend should be running at: http://localhost:3000.

The backend should be running at: http://localhost:8000.

# Contributing

You can spread the word about the project on social media, show your love by starring the repository, help with design and documentation, or contribute code.

For more information on contributing code, [check out our contributing guide](/CONTRIBUTING.md).

# Credits

TranscribeIt would not exist without these amazing projects:
- [yt-dlp](https://pypi.org/project/yt-dlp) for supporting multiple online video streaming platforms
- [faster-whisper](https://pypi.org/project/faster-whisper) for timestamped, mutli-lingual transcriptions
- [Chakra UI](https://www.chakra-ui.com/) for accessible UI components
- [FastAPI](https://fastapi.tiangolo.com/) for rapid API development
- [Next.js](https://nextjs.org) for frontend framework

# License

TranscribeIt is licensed under GNU Affero General Public License version 3. For more information, [check out our LICENSE file](./LICENSE).