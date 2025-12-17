import * as v from "valibot"
import { TranscriptResponseSchema } from "./schema"
import { TranscriptRequest, TranscriptResponse, TranscriptionData } from "./types"

export const formatTime = (seconds: number): string => {
    const totalSeconds = Math.round(seconds);
    const minutes = Math.floor(totalSeconds / 60);
    const remainingSeconds = totalSeconds % 60;
    return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
}

export const getTranscription = async (url: TranscriptRequest) => {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/transcribe/url`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(url),
      }
    );
    if (!response.ok) {
        throw new Error(`An error occurred while fetching transcription. Status code: ${response.status}`)
    }
    const data = v.parse(TranscriptResponseSchema, await response.json())
    if (!data.success) {
        throw new Error("Failed to fetch transcript response")
    }
    const content: TranscriptionData = data.data || []
    return content
};
