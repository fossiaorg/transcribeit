import * as v from "valibot";

export const TranscriptionDataSchema = v.array(
  v.object({
    start: v.number(),
    end: v.number(),
    text: v.string(),
  })
)

export const TranscriptRequestSchema = v.object({
  url: v.string(),
});

export const TranscriptResponseSchema = v.object({
  success: v.boolean(),
  message: v.string(),
  data: v.optional(TranscriptionDataSchema),
});
