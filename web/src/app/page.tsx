'use client';
import { useState, ChangeEvent } from 'react';
import {
  Box,
  Button,
  Input,
  Text,
  VStack,
  Spinner,
  FormControl,
  FormLabel,
  FormHelperText,
  FormErrorMessage,
  Stack,
  Divider,
} from '@chakra-ui/react';
import { getTranscription, getTranscriptionFromFile } from '@/lib/utils';
import { TranscriptionData } from '@/lib/types';
import Transcription from '@/components/app/Transcription';

export default function Home() {
  const [url, setUrl] = useState<string>('');
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [transcription, setTranscription] = useState<TranscriptionData | null>(
    null
  );
  const [error, setError] = useState<string | null>(null);
  const [validationError, setValidationError] = useState<string | null>(null);

  const handleTranscribe = async () => {
    // Validation: ensure only one input method is used
    if (!url && !file) {
      setValidationError('Please either enter a video URL or upload an audio file.');
      return;
    }

    if (url && file) {
      setValidationError('Please choose only one input: URL or file upload.');
      return;
    }

    setValidationError(null);
    setLoading(true);
    setError(null);
    setTranscription(null);

    try {
      let data: TranscriptionData;
      
      if (file) {
        data = await getTranscriptionFromFile(file);
      } else {
        data = await getTranscription({ url: url });
      }
      
      if (data) {
        setTranscription(data);
      } else {
        setError('Failed to transcribe.');
      }
    } catch (err) {
      console.error('Error during transcription:', err);
      const fallbackMessage = 'An error occurred while processing the request.';
      const message =
        err instanceof Error && err.message ? err.message : fallbackMessage;
      setError(message);
    } finally {
      setLoading(false);
    }
  };

  const handleUrlChange = (e: ChangeEvent<HTMLInputElement>) => {
    setUrl(e.target.value);
    setValidationError(null);
    // Clear file if URL is entered
    if (e.target.value && file) {
      setFile(null);
    }
  };

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0] || null;
    setFile(selectedFile);
    setValidationError(null);
    if (selectedFile && url) {
      setUrl('');
    }
  };

  const handleClearFile = () => {
    setFile(null);
    setValidationError(null);
  };

  return (
    <VStack align="center" p={16} w="full" color="blackAlpha.800">
      <Box w="full" h="full" maxW="70%" p={6} borderRadius="md" boxShadow="md">
        <Text fontSize="2xl" fontWeight="bold" mb={4} textAlign="center">
          Transcribe Videos & Audio Files
        </Text>

        <Stack gap={6}>
          <FormControl isInvalid={!!validationError}>
            <FormLabel>Enter Video URL</FormLabel>
            <Input
              value={url}
              onChange={handleUrlChange}
              placeholder="Paste video URL here"
              size="lg"
              isDisabled={!!file || loading}
            />
            <FormHelperText>
              Enter a video URL from supported platforms
            </FormHelperText>
          </FormControl>

          <Box position="relative">
            <Divider />
            <Box
              position="absolute"
              top="50%"
              left="50%"
              transform="translate(-50%, -50%)"
              bg="white"
              px={4}
            >
              <Text fontSize="sm" color="gray.500">
                OR
              </Text>
            </Box>
          </Box>

          <FormControl isInvalid={!!validationError}>
            <FormLabel>Upload Audio File</FormLabel>
            <Input
              type="file"
              accept="audio/*,video/*"
              onChange={handleFileChange}
              size="lg"
              pt={1}
              isDisabled={!!url || loading}
              sx={{
                '::file-selector-button': {
                  height: '100%',
                  padding: '8px 16px',
                  marginRight: '12px',
                  border: 'none',
                  borderRadius: 'md',
                  backgroundColor: 'blue.500',
                  color: 'white',
                  cursor: 'pointer',
                  _hover: {
                    backgroundColor: 'blue.600',
                  },
                  _disabled: {
                    backgroundColor: 'gray.300',
                    cursor: 'not-allowed',
                  },
                },
              }}
            />
            {file && (
              <Box mt={2}>
                <Text fontSize="sm" color="gray.600">
                  Selected: {file.name}
                </Text>
                <Button
                  size="sm"
                  colorScheme="red"
                  variant="ghost"
                  onClick={handleClearFile}
                  mt={1}
                  isDisabled={loading}
                >
                  Clear file
                </Button>
              </Box>
            )}
            <FormHelperText>
              Upload an audio or video file from your computer
            </FormHelperText>
            {validationError && (
              <FormErrorMessage>{validationError}</FormErrorMessage>
            )}
          </FormControl>

          <Button
            bgColor={'blue.500'}
            onClick={handleTranscribe}
            loadingText="Transcribing..."
            disabled={loading || (!url && !file)}
            size="lg"
            _hover={{ bgColor: 'blue.600' }}
          >
            {loading && <Spinner size="sm" mr={2} />}
            {loading ? 'Transcribing...' : file ? 'Transcribe File' : 'Transcribe Video'}
          </Button>
        </Stack>

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
