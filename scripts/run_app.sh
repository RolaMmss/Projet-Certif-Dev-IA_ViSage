#!/bin/bash

set -o allexport
# Load environment variables from .env file
source .env   
set +o allexport

# Pull the latest image from Docker Hub
docker pull $DOCKERHUB_USERNAME/repo_docker:latest

# Run the Docker container with port mapping and other configurations
docker run -d --name webapp_container \
  -p 8000:8000 \
  $DOCKERHUB_USERNAME/repo_docker:latest
