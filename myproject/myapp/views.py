# Importation des modules Django nécessaires
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignupForm,LoginForm, ApiForm
from . import forms
import json
from dotenv import load_dotenv
import os
import requests
from django.contrib.auth.decorators import login_required
from .models import ImagePrediction
from django.http import JsonResponse
import logging
from django.utils import timezone
from myproject.opentelemetry_setup import prediction_counter_per_minute, logger, tracer

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
#########################################################
# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

# Récupération des identifiants du client à partir des variables d'environnement
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
# url_api = os.getenv('URL_API')
url_api='https://api.everypixel.com/v1/faces'

logger = logging.getLogger(__name__)
#########################################################
def hello(request):

    return HttpResponse(f"""
        <h1>Hello Rola!</h1>
""")

@login_required
def homepage(request):
    return render(request, 'myapp/homepage.html')

#########################################################
def signup(request):
    """Create a signup page view for the app.

    Args:
        request (HttpRequest): The HTTP request.
    
    Returns:
        HttpResponse: The HTTP response with the rendered signup page.    """
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            logger.info(f"User {user.username} signed up and logged in")
            return redirect('login')
    return render(request, 'myapp/signup.html', context={'form': form})
#####################################################################
def login_user(request):
    """The function login_page takes a request object and renders the login.html template with a LoginForm instance and a message. If the request method is POST, the form is validated and the user is authenticated using the provided username and password. If the authentication is successful, the user is logged in and redirected to the home page. Otherwise, an error message is displayed.
        The coach is staff and may sign in with:
            Username: Dr.Django
            Password: passworddjango
    Parameters:
        request: the HTTP request object sent by the client.

    Returns: 
        HttpResponse object that represents the rendered response of the login.html template.
    """
    form = LoginForm()
    message= ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                logger.info(f"User {user.username} logged in")
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('home')
            else:
                logger.warning("Invalid login attempt")
                # message = 'Identifiants invalides.'
                # Add an error message to the form
                form.add_error(None, 'Identifiants invalides.')
    return render(request, 'myapp/login.html', context={'form': form,'message':message})
#########################################################################""
def logout_user(request):
    """Log out the currently authenticated user and redirect them to the login page.

    Args:
        request: The HTTP request object.
    Returns:
        A redirect response to the login page.
    """
    logger.info("User logged out")
    logout(request)
    return redirect('login')
############################################################################
#ORIGINAL
# # Décorateur pour exiger l'authentification de l'utilisateur
# @login_required
# def api(request):
#     if request.method == 'POST':
#         form = ApiForm(request.POST)
#         if form.is_valid():
#             image_url = form.cleaned_data['image_url']
#             response = requests.get(url_api, params={'url': image_url}, auth=(CLIENT_ID, CLIENT_SECRET))
#             # Log the response content
#             print(response.content)
#             prediction_data = json.loads(response.text).get('faces', [])

#             # Save prediction data to the database
#             prediction_instance = ImagePrediction.objects.create(image_url=image_url, prediction_data=prediction_data)

#             # Convert the timestamp to local time
#             local_time = timezone.localtime(prediction_instance.timestamp)

#             return render(
#                 request,
#                 'myapp/reponse_formulaire.html',
#                 context={'form': form, 'info': prediction_data, 'nombre_personne': len(prediction_data), 'url': image_url, 'timestamp': local_time}
#             )
#     else:
#         form = ApiForm()

#     return render(request, 'myapp/formulaire.html', context={'form': form})

# Décorateur pour exiger l'authentification de l'utilisateur


# # Décorateur pour exiger l'authentification de l'utilisateur
# @login_required
# def api(request):
#     if request.method == 'POST':
#         form = ApiForm(request.POST)
#         if form.is_valid():
#             with tracer.start_as_current_span("form_processing"):
#                 image_url = form.cleaned_data['image_url']
#                 # Log the received image URL
#                 logger.info(f"Image URL received: {image_url}")
#                 with tracer.start_as_current_span("external_api_request"):
#                     response = requests.get(url_api, params={'url': image_url}, auth=(CLIENT_ID, CLIENT_SECRET))
#                     # Log the response content
#                     print(response.content)
#                     prediction_data = json.loads(response.text).get('faces', [])
#                     # Log the prediction result
#                     logger.info(f"Prediction Data: {prediction_data}")
#                     # Save prediction data to the database
#                     prediction_instance = ImagePrediction.objects.create(image_url=image_url, prediction_data=prediction_data)

#                     # Convert the timestamp to local time
#                     local_time = timezone.localtime(prediction_instance.timestamp)
#                     # Record prediction metrics
#                     prediction_counter_per_minute.add(1)
                
#                     return render(
#                         request,
#                         'myapp/reponse_formulaire.html',
#                         context={'form': form, 'info': prediction_data, 'nombre_personne': len(prediction_data), 'url': image_url, 'timestamp': local_time}
#                     )
#     else:
#         form = ApiForm()
#     return render(request, 'myapp/formulaire.html', context={'form': form})

# Décorateur pour exiger l'authentification de l'utilisateur


# @login_required
# def api(request):
#     form = ApiForm()  # Initialize form variable

#     with tracer.start_as_current_span("api_span"):
#         url_api = os.getenv('URL_API')
#         client_id = os.getenv('CLIENT_ID')
#         client_secret = os.getenv('CLIENT_SECRET')

#         if not url_api or not client_id or not client_secret:
#             logger.error("Missing environment variables.")
#             return render(request, 'myapp/formulaire.html', {'form': form, 'error': 'Configuration error'})

#         if request.method == 'POST':
#             form = ApiForm(request.POST)
#             if form.is_valid():
#                 with tracer.start_as_current_span("form_processing"):
#                     image_url = form.cleaned_data['image_url']
#                     # Log the received image URL
#                     logger.info(f"Image URL received: {image_url}")
#                     with tracer.start_as_current_span("external_api_request"):
#                         response = requests.get(url_api, params={'url': image_url}, auth=(CLIENT_ID, CLIENT_SECRET))
#                         # # Log the response content
#                         # print(response.content)
#                         prediction_data = json.loads(response.text).get('faces', [])
#                         # Log the prediction result
#                         logger.info(f"Prediction Data: {prediction_data}")
#                         # Save prediction data to the database
#                         prediction_instance = ImagePrediction.objects.create(image_url=image_url, prediction_data=prediction_data)
#                         # Convert timestamp to local time
#                         local_time = timezone.localtime(prediction_instance.timestamp)
#                         # Record prediction metrics
#                         prediction_counter_per_minute.add(1)
                
#                         return render(
#                             request,
#                             'myapp/reponse_formulaire.html',
#                             context={'form': form, 'info': prediction_data, 'nombre_personne': len(prediction_data), 'url': image_url, 'timestamp': local_time}
#                         )
#             else:
#                 form = ApiForm()

#         return render(request, 'myapp/formulaire.html', context={'form': form})

# Set up the Meter Provider
metrics.set_meter_provider(MeterProvider())
meter = metrics.get_meter(__name__)
# Create a counter for daily predictions
prediction_counter_per_day = meter.create_counter("prediction_counter_per_day")
# Create a histogram to record the time taken for predictions
prediction_latency = meter.create_histogram("prediction_latency")



# def api(request):
#     if request.method == 'POST':
#         form = ApiForm(request.POST)
#         if form.is_valid():
#             with tracer.start_as_current_span("form_processing"):
#                 image_url = form.cleaned_data['image_url']
#                 # Log the received image URL
#                 logger.info(f"Image URL received: {image_url}")
#                 with tracer.start_as_current_span("external_api_request"):
#                     response = requests.get(url_api, params={'url': image_url}, auth=(CLIENT_ID, CLIENT_SECRET))
                    
#                     # # Log the response content
#                     # logger.info(f"API Response: {response.content}")
                    
#                     # Check if the response contains age information
#                     prediction_data = json.loads(response.text).get('faces', [])
                    
#                     # Log prediction data
#                     logger.info(f"Prediction Data: {prediction_data}")

#                     # Save prediction data to the database
#                     prediction_instance = ImagePrediction.objects.create(image_url=image_url, prediction_data=prediction_data)

#                     # Convert the timestamp to local time
#                     local_time = timezone.localtime(prediction_instance.timestamp)
#                     # Record prediction metrics
#                     prediction_counter_per_minute.add(1)
#                     prediction_counter_per_day.add(1)
#                     return render(
#                         request,
#                         'myapp/reponse_formulaire.html',
#                         context={'form': form, 'info': prediction_data, 'nombre_personne': len(prediction_data), 'url': image_url, 'timestamp': local_time}
#                     )
#     else:
#         form = ApiForm()

#     return render(request, 'myapp/formulaire.html', context={'form': form})



def api(request):
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            # Start tracing for form processing
            with tracer.start_as_current_span("form_processing") as span:
                image_url = form.cleaned_data['image_url']
                
                # Log the image URL received
                logger.info(f"Image URL received: {image_url}")
                
                # Start tracing for the external API request
                with tracer.start_as_current_span("external_api_request") as api_span:
                    try:
                        response = requests.get(
                            url_api, 
                            params={'url': image_url}, 
                            auth=(CLIENT_ID, CLIENT_SECRET)
                        )
                        response.raise_for_status()  # Raise an exception for any HTTP errors
                        
                        # Log the response status and content
                        logger.info(f"API Response Status: {response.status_code}")
                        logger.debug(f"API Response Content: {response.content}")
                        
                    except requests.exceptions.RequestException as e:
                        logger.error(f"API Request failed: {e}")
                        # Add an event to the span to track the error
                        api_span.add_event("API Request Failure", attributes={"error": str(e)})
                        return render(
                            request, 
                            'myapp/error_page.html', 
                            context={'form': form, 'error_message': 'Failed to retrieve predictions from the API.'}
                        )
                    
                    # Parse the prediction data
                    prediction_data = json.loads(response.text).get('faces', [])
                    
                    # Log prediction data
                    logger.info(f"Prediction Data: {prediction_data}")
                    
                    # Save prediction data to the database
                    try:
                        with tracer.start_as_current_span("db_save") as db_span:
                            prediction_instance = ImagePrediction.objects.create(
                                image_url=image_url, 
                                prediction_data=prediction_data
                            )
                            
                            # Convert the timestamp to local time
                            local_time = timezone.localtime(prediction_instance.timestamp)
                            # Log successful database save
                            logger.info(f"Prediction saved to DB at {local_time}")
                    
                    except Exception as db_error:
                        logger.error(f"Failed to save prediction data: {db_error}")
                        db_span.add_event("DB Save Failure", attributes={"error": str(db_error)})
                        return render(
                            request, 
                            'myapp/error_page.html', 
                            context={'form': form, 'error_message': 'Failed to save prediction to the database.'}
                        )
                    
                    # Record prediction metrics
                    prediction_counter_per_minute.add(1)
                    prediction_counter_per_day.add(1)

                    # Render the response form with prediction data
                    return render(
                        request,
                        'myapp/reponse_formulaire.html',
                        context={
                            'form': form,
                            'info': prediction_data,
                            'nombre_personne': len(prediction_data),
                            'url': image_url,
                            'timestamp': local_time
                        }
                    )
    else:
        form = ApiForm()
    # Render the initial form
    return render(request, 'myapp/formulaire.html', context={'form': form})
