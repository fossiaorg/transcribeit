import React from "react";
import { Box, Text, VStack, Flex, Spacer } from "@chakra-ui/react";
import { TranscriptionData } from "@/lib/types";
import { formatTime } from "@/lib/utils";

interface TranscriptionProps {
  data: TranscriptionData;
}

const Transcription: React.FC<TranscriptionProps> = ({ data }) => {
  return (
    <>
      <Text fontSize="lg" fontWeight="bold" mb="2">
        Transcription
      </Text>
      <VStack
        align="start"
        padding={4}
        borderRadius="md"
        backgroundColor="gray.50"
      >
        {data.map((item, index) => (
          <Box
            key={index}
            width="100%"
            p={4}
            borderWidth="1px"
            borderRadius="md"
            backgroundColor="white"
          >
            <Flex direction="row" mb={2} spaceX={2}>
              <Text mt={2} textStyle={"xl"}>
                {`${formatTime(item.start)} - ${formatTime(item.end)}`}
              </Text>
              <Text fontSize="lg" mt={2}>
                {`${item.text}`}
              </Text>
            </Flex>
          </Box>
        ))}
      </VStack>
    </>
  );
};

export default Transcription;
