# #!/bin/bash

# set -o allexport
# # Load environment variables from .env file
# source .env   
# set +o allexport

# # Pull the latest image from Docker Hub
# docker pull $DOCKERHUB_USERNAME/repo_webapp:latest

# # Run the Docker container with port mapping and other configurations
# docker run -d --name webappcontainer \
# -p 8000:8000 \
# $DOCKERHUB_USERNAME/repo_webapp:latest

# # Run it: chmod +x scripts/run_app.sh
# # Execute it : ./scripts/run_app.sh