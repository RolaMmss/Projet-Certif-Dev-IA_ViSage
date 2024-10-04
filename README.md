# Projet-Certif-Dev-IA_ViSage
Projet d'Intelligence Artificielle - Mise en Service, Développement d'Application et Débogage.

Develop a web app that integrates an artificial intelligence model, monitor this model, program automated tests, and create a continuous delivery pipeline for this AI model in an MLOps approach to automate the steps of validation, testing, packaging, and deployment of the app.


# Create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate

# Install all dependencies    
- pip freeze > requirements.txt    ---> captures the current state of installed packages and their specific versions in a virtual environment

- pip install -r requirements.txt  ---> install packages in requirements.txt

# Run the pytests : 

Change directory to myproject
pytest tests/test_views.py

<!-- PYTHONPATH=./ pytest myproject/tests
        ( in case it didn't find api, this will lead to the correct path) -->

# Launch the web app
python manage.py runserver --noreload

## Deploy the Web App
- Build and test the Docker Image locally: 
        docker build -t imagewebapp:latest -f Dockerfile . 
        docker run -p 8000:8000 imagewebapp:latest

        - then /docs
        Remark: Each time you build a new image, you have to go to Docker extension in vscode to delete the existant containers:
        docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)

- Test docker run with environment variables locally:
docker run -p 8000:8000 \
    -e CLIENT_ID=WGY8DrcNMzq6vr4JYFoGioeB \
    -e CLIENT_SECRET=3qxldq8wTZhVdAxGtnvJpf1fKJNEHbZty9dTWACnehhAw10B \
    imageweb:latest

docker run -p 8000:8000 -e "APPLICATIONINSIGHTS_CONNECTION_STRING=InstrumentationKey=25155d74-cfca-43aa-b788-aa2ca8de59d7;IngestionEndpoint=https://francecentral-1.in.applicationinsights.azure.com/;LiveEndpoint=https://francecentral.livediagnostics.monitor.azure.com/;ApplicationId=2e13bbed-3d25-4592-ab6c-1558e02b2ca8" imageweb:latest

- Tag the image before pushing it to dockerhub
        - docker login
        - docker tag imagewebapp rola123/imagewebapp:latest
        - docker push rola123/imagewebapp:latest

# Create Azure Container Instance
Execute create_ACI.sh in the terminal as follows:
    cd to the directory root next to api,model, .env, etc...
    chmod +x scripts/create_ACI.sh
    ./scripts/create_ACI.sh
# Go to Azure container instance, check the existance of the deployed app the type the followint in browser to lauch the App:
 http://myapp-container.francecentral.azurecontainer.io:8000/
 
   # superuser:  
   username : Rola
   
   password : passwordrola

# CI/CD
- GitHub Actions workflows are set up to trigger on pushes to the main, develop, and test-traces branches and for changes in the myproject/** directory or .github/workflows/ files. 

- If you want the workflow to trigger on every push regardless of which files were changed, remove the paths filter.

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