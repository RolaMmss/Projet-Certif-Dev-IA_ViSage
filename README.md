# Projet-Certif-Dev-IA_ViSage
Projet d'Intelligence Artificielle - Mise en Service, Développement d'Application et Débogage

# Create and activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Run the pytests : 
pytest myapp/tests.py

<!-- PYTHONPATH=./ pytest myapp/tests/          ( in case it didn't find api, this will lead to the correct path) -->

# Launch the web app
python3 manage.py runserver

## Deploy the Web App
- Build and test the Docker Image locally: 
        - docker build -t imageweb:latest -f Dockerfile .
        - docker run -p 8000:8000 imageweb:latest
        - then /docs
        Remark: Each time you build a new image, you have to go to Docker extension in vscode to delete the existant containers.
- Tag the image before pushing it to dockerhub
        - docker login
        - docker tag imageweb rola123/repo_docker:v1
        - docker push rola123/repo_docker:v1

# Create Azure Container Instance
Execute create_ACR.sh in the terminal as follows:
    cd to the directory root next to api,model, .env, etc...
    chmod +x scripts/create_ACI.sh
    ./scripts//create_ACI.sh

# http://myapp-container.francecentral.azurecontainer.io:8000/
        

# CI/CD with Github Actions
# Get Azure credentials
az login
az ad sp create-for-rbac --name myproject-sp --sdk-auth
(# Create a service principal
az ad sp create-for-rbac --name github-actions-aci --role contributor --scopes /subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/YOUR_RESOURCE_GROUP --sdk-auth)
