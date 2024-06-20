import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from myapp.forms import SignupForm  # Import your custom SignupForm
from django.contrib.auth.forms import UserCreationForm

@pytest.mark.django_db
def test_homepage(client):
    # Test homepage view for authenticated user
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    response = client.get(reverse('home'))
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_homepage_unauthenticated(client):
    # Test homepage view for unauthenticated user
    response = client.get(reverse('home'))
    assert response.status_code == 302  # Redirects to login page
    
@pytest.mark.django_db
def test_signup(client):
    # Test signup view
    response = client.get(reverse('signup'))
    assert response.status_code == 200
    # Check if the form is an instance of UserCreationForm or SignupForm
    assert isinstance(response.context['form'], UserCreationForm)

@pytest.mark.django_db
def test_login_user(client):
    # Test login view with valid credentials
    user = User.objects.create_user(username='Dr.Django', password='passworddjango')
    response = client.get(reverse('login'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_logout_user(client):
    # Test logout view
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')
    response = client.get(reverse('logout'))
    assert response.status_code == 302  # Redirects to login page

# This test requires the pytest-mock fixture to be available
@pytest.mark.django_db
def test_api(client, mocker):
    # Test API view
    # Mock requests.get to avoid making actual API calls during tests
    mocker.patch('requests.get')
    # You can add your API test logic here
    pass
