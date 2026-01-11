'use client';
import { useState, ChangeEvent } from 'react';
import {
  Box,
  Button,
  Input,
  Text,
  VStack,
  Spinner,
} from '@chakra-ui/react';
import { getTranscription } from '@/lib/utils';
import { TranscriptionData } from '@/lib/types';
import Transcription from '@/components/app/Transcription';

export default function Home() {
  const [url, setUrl] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [transcription, setTranscription] = useState<TranscriptionData | null>(
    null
  );
  const [error, setError] = useState<string | null>(null);

  const handleTranscribe = async () => {
    if (!url) return;

    setLoading(true);
    setError(null);
    setTranscription(null);

    try {
      const data: TranscriptionData = await getTranscription({ url: url });
      if (data) {
        setTranscription(data);
      } else {
        setError('Failed to transcribe video.');
      }
    } catch (err) {
      setError('An error occurred while processing the request.');
    } finally {
      setLoading(false);
    }
  };

  const handleUrlChange = (e: ChangeEvent<HTMLInputElement>) => {
    setUrl(e.target.value);
  };

  return (
    <VStack align="center" p={16} w="full">
      <Box w="full" h="full" maxW="70%" p={6} borderRadius="md" boxShadow="md">
        <Text fontSize="2xl" fontWeight="bold" mb={4} textAlign="center">
          Transcribe online videos
        </Text>

        <Input
          value={url}
          name="Paste video URL here for transcription"
          onChange={handleUrlChange}
          placeholder="Paste video URL here for transcription"
          size="lg"
          mb={4}
        />

          <Button
            bgColor={'blue.500'}
            onClick={handleTranscribe}
            loadingText="Transcribing..."
            disabled={loading}
          >
            {loading && <Spinner/>}
            Transcribe Video
          </Button>

        {error && (
          <Text color="red.500" mt={4}>
            {error}
          </Text>
        )}
        {transcription && (
          <Box mt={6}>
            <Transcription data={transcription}></Transcription>
          </Box>
        )}
      </Box>
    </VStack>
  );
}
