# Importation des modules Django nécessaires
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignupForm,LoginForm
from . import forms
import json
from dotenv import load_dotenv
import os
import requests
from django.contrib.auth.decorators import login_required

#########################################################
# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

# Récupération des identifiants du client à partir des variables d'environnement
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

#########################################################
def hello(request):

    return HttpResponse(f"""
        <h1>Hello Django from container!</h1>
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
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(request, 'myapp/login.html', context={'form': form,'message':message})
#########################################################################""
def logout_user(request):
    """Log out the currently authenticated user and redirect them to the login page.

    Args:
        request: The HTTP request object.
    Returns:
        A redirect response to the login page.
    """
    logout(request)
    return redirect('login')
############################################################################
# Décorateur pour exiger l'authentification de l'utilisateur
# @login_required
def api(request):
    # Affichage des identifiants du client dans la console (à des fins de débogage)
    print(CLIENT_ID)
    print(CLIENT_SECRET)

    # URL de l'API à interroger
    url_api = "https://api.everypixel.com/v1/faces"

    # Vérification du type de requête HTTP
    if request.method == "POST":
        # Initialisation du formulaire avec les données de la requête POST
        form = forms.ApiForm(request.POST)
        if form.is_valid():
            # Affichage des données nettoyées du formulaire (à des fins de débogage)
            print(form.cleaned_data)

            # Envoi de la requête à l'API en utilisant les identifiants du client
            response = requests.get(url_api, params=form.cleaned_data, auth=(CLIENT_ID, CLIENT_SECRET))
            
            # Sauvegarde du formulaire après la requête
            form.save()

            # Utilisation de .get() pour éviter une KeyError si la clé 'faces' n'est pas présente
            info = json.loads(response.text).get("faces", [])

            # Affichage des informations récupérées (à des fins de débogage)
            print(info)
            print(form.cleaned_data)

            # Rendu de la page avec les résultats
            return render(
                request,
                'myapp/reponse_formulaire.html',
                context={'form': form, 'info': info, 'nombre_personne': len(info), 'url': form.cleaned_data['url']}
            )

    else:
        # Initialisation d'un formulaire vide en cas de requête GET
        form = forms.ApiForm()

    # Rendu de la page avec le formulaire
    return render(request, 'myapp/formulaire.html', context={'form': form})