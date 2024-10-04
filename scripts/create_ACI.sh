# #!/bin/bash
# # create_ACI.sh

# # Load environment variables from .env file
# if [ -f .env ]; then
#     source .env
# else
#     echo ".env file not found"
#     exit 1
# fi

# # Azure Container Instance (ACI) configuration
# RESOURCE_GROUP="$RESSOURCE_GROUP"  # Ensure this matches your Azure resource group name
# ACI_NAME="myapp-container"         # Name for your ACI
# CONTAINER_IMAGE="$DOCKERHUB_USERNAME/repo_docker:v1"

# # Check if required variables are set
# if [[ -z "${DOCKERHUB_USERNAME}" ]] || [[ -z "${DOCKERHUB_PASSWORD}" ]] || \
#    [[ -z "${SUBSCRIPTION_ID}" ]] || [[ -z "${RESSOURCE_GROUP}" ]]; then
#     echo "Required environment variables not set in .env file"
#     exit 1
# fi

# # Login to Dockerhub
# echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin

# # Create ACI with Azure CLI
# az container create \
#     --resource-group "$RESOURCE_GROUP" \
#     --name "$ACI_NAME" \
#     --image "$CONTAINER_IMAGE" \
#     --cpu 1 \
#     --memory 1.5 \
#     --port 8000 \
#     --environment-variables \
#     DOCKERHUB_USERNAME="$DOCKERHUB_USERNAME" \
#     DOCKERHUB_PASSWORD="$DOCKERHUB_PASSWORD" \
#     SUBSCRIPTION_ID="$SUBSCRIPTION_ID" \
#     --os-type Linux \
#     --restart-policy OnFailure \
#     --dns-name-label "$ACI_NAME" \
#     --output json

# echo "ACI deployment created successfully."

#---------------------------------------------
set -o allexport
# Load environment variables from .env file
source .env   
set +o allexport

# Login to Azure
az login

az container create \
    --resource-group $RESSOURCE_GROUP \
    --name containerinstancewebapp \
    --image $DOCKERHUB_USERNAME/imagewebapp:latest \   
    --cpu 1 \
    --memory 1 \
    --ip-address public \
    --ports 80 8000 \
    --registry-username $DOCKERHUB_USERNAME \
    --registry-password $DOCKERHUB_PASSWORD

# Run it: chmod +x scripts/create_ACI.sh
# Execute it : ./scripts/create_ACI.sh