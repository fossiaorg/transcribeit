"use client"

import { Box, Flex, Heading, Button, Spacer, useBreakpointValue } from "@chakra-ui/react";
import { FaFile, FaGithub } from "react-icons/fa"

export default function Header() {
  let headingSize = useBreakpointValue({ base: "md", md: "lg" });
  if (!headingSize) {
    headingSize = "md"
  }
  return (
    <Box bg="blue.500" w="100%" p={4} color="white">
      <Flex align="center">
        <Heading as="h1" size="lg">
          TranscribeIt
        </Heading>
        <Spacer />
        <Button colorScheme="blue" mr={4} variant={"plain"} color="white">
          <FaGithub/> GitHub
        </Button>
        <Button colorScheme="blue" variant={"plain"} color="white">
          <FaFile/> Docs
        </Button>
      </Flex>
    </Box>
  );
};
