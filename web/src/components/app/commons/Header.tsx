"use client";

import {
	Box,
	Flex,
	Heading,
	Spacer,
	useBreakpointValue,
  Link,
} from "@chakra-ui/react";
import { FaFile, FaGitAlt } from "react-icons/fa";


export default function Header() {
	let headingSize = useBreakpointValue({ base: "md", md: "lg" });
	if (!headingSize) {
		headingSize = "md";
	}
	return (
		<header>
			<Box bg="blue.500" w="100%" p={4} color="white">
				<Flex align="center">
					<Heading as="h1" size="lg">
						TranscribeIt
					</Heading>
					<Spacer />
					<Link colorScheme="blue" mr={4} variant={"plain"} color="white" href="https://codeberg.org/fossiaorg/transcribeit">
						<FaGitAlt /> Source Code
					</Link>
					<Link colorScheme="blue" variant={"plain"} color="white" href="https://docs.transcribeit.fossia.org/">
						<FaFile /> Docs
					</Link>
				</Flex>
			</Box>
		</header>
	);
}
