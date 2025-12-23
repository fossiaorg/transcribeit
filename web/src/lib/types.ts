import * as v from "valibot";

import { TranscriptRequestSchema, TranscriptFileRequestSchema, TranscriptResponseSchema, TranscriptionDataSchema } from "./schema";

export type TranscriptionData = v.InferOutput<typeof TranscriptionDataSchema>;
export type TranscriptRequest = v.InferOutput<typeof TranscriptRequestSchema>;
export type TranscriptFileRequest = v.InferOutput<typeof TranscriptFileRequestSchema>;
export type TranscriptResponse = v.InferOutput<typeof TranscriptResponseSchema>;