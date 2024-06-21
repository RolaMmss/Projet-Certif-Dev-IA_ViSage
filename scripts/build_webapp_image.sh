# build_webapp_image.sh

set -o allexport
source .env
set +o allexport

# Warning: you need to update the path ./app_web to the path of your dockerfile
# Build and test the Docker image locally
docker build -t imageweb:latest -f Dockerfile .
docker run -p 8000:8000 imageweb:latest &

# Tag the image before pushing it to Docker Hub
docker login -u "$DOCKERHUB_USERNAME" -p "$DOCKERHUB_PASSWORD"
docker tag imageweb rola123/repo_docker:v1
docker push rola123/repo_docker:v1

# Run it: chmod +x build_webapp_image.sh
# Execute it : ./build_webapp_image.sh



# remark to be deleted