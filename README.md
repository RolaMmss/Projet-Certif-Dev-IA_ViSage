# Projet-Certif-Dev-IA_ViSage
Projet d'Intelligence Artificielle - Mise en Service, Développement d'Application et Débogage.

Develop a web app that integrates an artificial intelligence model, monitor this model, program automated tests, and create a continuous delivery pipeline for this AI model in an MLOps approach to automate the steps of validation, testing, packaging, and deployment of the app.


# Create and activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Run the pytests : 

Change directory to myproject
pytest tests/test_views.py

<!-- PYTHONPATH=./ pytest myproject/tests
        ( in case it didn't find api, this will lead to the correct path) -->

# Launch the web app
python3 manage.py runserver

## Deploy the Web App
- Build and test the Docker Image locally: 
        - docker build -t imagewebapp:latest -f Dockerfile .
        - docker run -p 8000:8000 imagewebapp:latest
        - then /docs
        Remark: Each time you build a new image, you have to go to Docker extension in vscode to delete the existant containers.
- Test docker run with environment variables locally:
docker run -p 8000:8000 \
    -e CLIENT_ID=WGY8DrcNMzq6vr4JYFoGioeB \
    -e CLIENT_SECRET=3qxldq8wTZhVdAxGtnvJpf1fKJNEHbZty9dTWACnehhAw10B \
    imageweb:latest

docker run -p 8000:8000 -e "APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=25155d74-cfca-43aa-b788-aa2ca8de59d7;IngestionEndpoint=https://francecentral-1.in.applicationinsights.azure.com/;LiveEndpoint=https://francecentral.livediagnostics.monitor.azure.com/;ApplicationId=2e13bbed-3d25-4592-ab6c-1558e02b2ca8" imageweb:latest

- Tag the image before pushing it to dockerhub
        - docker login
        - docker tag imageweb rola123/imageweb:latest
        - docker push rola123/imageweb:latest

# Create Azure Container Instance
Execute create_ACI.sh in the terminal as follows:
    cd to the directory root next to api,model, .env, etc...
    chmod +x scripts/create_ACI.sh
    ./scripts/create_ACI.sh

 http://myapp-container.francecentral.azurecontainer.io:8000/
   # superuser:  
   username : Rola
   
   password : passwordrola

# Monitoring
## Intégration de OpenTelemetry et Azure Application Insights

1. Installer les dépendances nécessaires:

pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-azure-monitor

Then install them: pip install -r requirements.txt

2. Configure OpenTelemetry via opentelemetry_setup.py

3. Load the configuration in settings.py

4. Set up environment variables:

APPLICATIONINSIGHTS_CONNECTION_STRING
and save it in .env (for local) and GitHub secrets (for deployed)

4. Add metrics and traces (views.py)

5. Verify the data in Azure Application Insights

Test test test