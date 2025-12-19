# Use the official Node.js image as a base image
FROM node:24-alpine AS builder

# Set the working directory inside the container
WORKDIR /frontend

# Copy package.json and yarn.lock
COPY package.json yarn.lock ./

# Install dependencies (including production and dev dependencies)
RUN yarn install --frozen-lockfile

# Copy the entire project into the container
COPY ./ ./

# Set environment variable
ARG NEXT_PUBLIC_BACKEND_URL
ENV NEXT_PUBLIC_BACKEND_URL=${NEXT_PUBLIC_BACKEND_URL}

# Build the Next.js application
RUN yarn build

# Use a smaller image for production
FROM node:24-alpine

# Set the working directory inside the container
WORKDIR /frontend

# Copy only the necessary files from the build stage
COPY --from=builder /frontend ./

# Install only production dependencies
RUN yarn install --production --frozen-lockfile

# Expose the port that the app will run on
EXPOSE 3000

# Set environment variable
ARG NEXT_PUBLIC_BACKEND_URL
ENV NEXT_PUBLIC_BACKEND_URL=${NEXT_PUBLIC_BACKEND_URL}

# Start the application in production mode
ENTRYPOINT ["yarn", "start"]
