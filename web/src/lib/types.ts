import * as v from "valibot";

import { TranscriptRequestSchema, TranscriptResponseSchema, TranscriptionDataSchema } from "./schema";

export type TranscriptionData = v.InferOutput<typeof TranscriptionDataSchema>;
export type TranscriptRequest = v.InferOutput<typeof TranscriptRequestSchema>;
export type TranscriptResponse = v.InferOutput<typeof TranscriptResponseSchema>;