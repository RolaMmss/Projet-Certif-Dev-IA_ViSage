# Projet-Certif-Dev-IA_ViSage
Projet d'Intelligence Artificielle - Mise en Service, Développement d'Application et Débogage

# Create and activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Run the pytests : 
pytest myapp/tests.py

<!-- PYTHONPATH=./ pytest myapp/tests.py         ( in case it didn't find api, this will lead to the correct path) -->

# Launch the web app
python3 manage.py runserver

## Deploy the Web App
- Build and test the Docker Image locally: 
        - docker build -t imageweb:latest -f Dockerfile .
        - docker run -p 8000:8000 imageweb:latest
        - then /docs
        Remark: Each time you build a new image, you have to go to Docker extension in vscode to delete the existant containers.
- Test docker run with environment variables locally:
docker run -p 8000:8000 \
    -e CLIENT_ID=WGY8DrcNMzq6vr4JYFoGioeB \
    -e CLIENT_SECRET=3qxldq8wTZhVdAxGtnvJpf1fKJNEHbZty9dTWACnehhAw10B \
    imageweb:latest

- Tag the image before pushing it to dockerhub
        - docker login
        - docker tag imageweb rola123/repo_webapp:latest
        - docker push rola123/repo_webapp:latest

# Create Azure Container Instance
Execute create_ACI.sh in the terminal as follows:
    cd to the directory root next to api,model, .env, etc...
    chmod +x scripts/create_ACI.sh
    ./scripts/create_ACI.sh

# http://myapp-container.francecentral.azurecontainer.io:8000/
        

