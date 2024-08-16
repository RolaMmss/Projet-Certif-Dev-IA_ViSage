
# # myapp/tests.py

# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from models import ImagePrediction
# from forms import SignupForm, LoginForm, ApiForm
# from unittest.mock import patch


# # Forms Tests:
# # SignupFormTest, LoginFormTest, and ApiFormTest check the validity of the forms with valid and invalid data.
# class SignupFormTest(TestCase):
#     def test_signup_form_valid(self):
#         form_data = {
#             'username': 'testuser',
#             'password1': 'complex_password123',
#             'password2': 'complex_password123',
#             'email': 'testuser@example.com',
#         }
#         form = SignupForm(data=form_data)
#         self.assertTrue(form.is_valid())

#     def test_signup_form_invalid(self):
#         form_data = {
#             'username': 'testuser',
#             'password1': 'complex_password123',
#             'password2': 'different_password',
#             'email': 'testuser@example.com',
#         }
#         form = SignupForm(data=form_data)
#         self.assertFalse(form.is_valid())

# class LoginFormTest(TestCase):
#     def test_login_form_valid(self):
#         form_data = {
#             'username': 'testuser',
#             'password': 'complex_password123',
#         }
#         form = LoginForm(data=form_data)
#         self.assertTrue(form.is_valid())

#     def test_login_form_invalid(self):
#         form_data = {
#             'username': '',
#             'password': 'complex_password123',
#         }
#         form = LoginForm(data=form_data)
#         self.assertFalse(form.is_valid())

# class ApiFormTest(TestCase):
#     def test_api_form_valid(self):
#         form_data = {'image_url': 'http://example.com/image.jpg'}
#         form = ApiForm(data=form_data)
#         self.assertTrue(form.is_valid())

#     def test_api_form_invalid(self):
#         form_data = {'image_url': ''}
#         form = ApiForm(data=form_data)
#         self.assertFalse(form.is_valid())
        
# # ------------------------------------------------------------------------------------------------------
# # Views Tests:
# #    - ViewsTest sets up a test client and user for testing views.
# #    - Tests include checking the response status code, used templates, and form handling.
# class ViewsTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = get_user_model().objects.create_user(username='testuser', password='complex_password123')
    
#     def test_hello_view(self):
#         response = self.client.get(reverse('hello'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Hello Rola!')

#     def test_signup_view(self):
#         response = self.client.get(reverse('signup'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'myapp/signup.html')

#     def test_login_view(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'myapp/login.html')

#     def test_api_view_get(self):
#         self.client.login(username='testuser', password='complex_password123')
#         response = self.client.get(reverse('myapp:myapp'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'myapp/formulaire.html')

#     @patch('requests.get')       # For the API view, the requests.get call is mocked to avoid making actual API requests during testing.
#     def test_api_view_post(self, mock_get):
#         self.client.login(username='testuser', password='complex_password123')
#         mock_response = mock_get.return_value
#         mock_response.status_code = 200
#         # mock_response.text = json.dumps({'faces': [{'confidence': 0.99}]})
#         mock_response.text = '{"faces":[{"bbox":[139.29549071043752,185.8942106522123,211.2634360686308,278.7116930608726],"score":0.9936680197715759,"age":39.74738493585028,"class":"Age - Adult"},{"bbox":[371.91275590162337,65.29337760344863,448.1290859205329,161.90829295588202],"score":0.9898697733879089,"age":69.0,"class":"Age - Senior Adult"}],"status":"ok"}'

#         response = self.client.post(reverse('myapp:myapp'), {'image_url': 'http://example.com/image.jpg'})
#         self.assertEqual(response.status_code, 200)
#     # Check for the presence of specific data in the response
#         self.assertContains(response, 'Age - Adult')
#         self.assertContains(response, 'Age - Senior Adult')

# # ------------------------------------------------------------------------------------------------------
# # Models Tests: verifies that the ImagePrediction model correctly stores and represents data.
# class ModelsTest(TestCase):
#     def test_image_prediction_model(self):
#         prediction_data = {
#             'faces': [
#                 {
#                     'bbox': [139.29549071043752, 185.8942106522123, 211.2634360686308, 278.7116930608726],
#                     'score': 0.9936680197715759,
#                     'age': 39.74738493585028,
#                     'class': 'Age - Adult'
#                 },
#                 {
#                     'bbox': [371.91275590162337, 65.29337760344863, 448.1290859205329, 161.90829295588202],
#                     'score': 0.9898697733879089,
#                     'age': 69.0,
#                     'class': 'Age - Senior Adult'
#                 }
#             ],
#             'status': 'ok'
#         }
#         prediction = ImagePrediction.objects.create(
#             image_url='http://example.com/image.jpg',
#             prediction_data=prediction_data
#         )
#         expected_string = ("Image URL: http://example.com/image.jpg - Predictions: "
#                            "{'faces': [{'bbox': [139.29549071043752, 185.8942106522123, 211.2634360686308, "
#                            "278.7116930608726], 'score': 0.9936680197715759, 'age': 39.74738493585028, 'class': 'Age - Adult'}, "
#                            "{'bbox': [371.91275590162337, 65.29337760344863, 448.1290859205329, 161.90829295588202], "
#                            "'score': 0.9898697733879089, 'age': 69.0, 'class': 'Age - Senior Adult'}], 'status': 'ok'}")

#         self.assertEqual(str(prediction), expected_string)
#------------------------------------------------------------

import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from myapp.models import ImagePrediction
from myapp.forms import SignupForm, LoginForm, ApiForm
from unittest.mock import patch

# Fixtures for setting up the client and user
@pytest.fixture
def client():
    return Client()

@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(username='testuser', password='complex_password123')

# Forms Tests:
@pytest.mark.django_db
def test_signup_form_valid():
    form_data = {
        'username': 'testuser',
        'password1': 'complex_password123',
        'password2': 'complex_password123',
        'email': 'testuser@example.com',
    }
    form = SignupForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_signup_form_invalid():
    form_data = {
        'username': 'testuser',
        'password1': 'complex_password123',
        'password2': 'different_password',
        'email': 'testuser@example.com',
    }
    form = SignupForm(data=form_data)
    assert not form.is_valid()

def test_login_form_valid():
    form_data = {
        'username': 'testuser',
        'password': 'complex_password123',
    }
    form = LoginForm(data=form_data)
    assert form.is_valid()

def test_login_form_invalid():
    form_data = {
        'username': '',
        'password': 'complex_password123',
    }
    form = LoginForm(data=form_data)
    assert not form.is_valid()

def test_api_form_valid():
    form_data = {'image_url': 'http://example.com/image.jpg'}
    form = ApiForm(data=form_data)
    assert form.is_valid()

def test_api_form_invalid():
    form_data = {'image_url': ''}
    form = ApiForm(data=form_data)
    assert not form.is_valid()
    
# Views Tests:
@pytest.mark.django_db
def test_hello_view(client):
    response = client.get(reverse('hello'))
    assert response.status_code == 200
    assert 'Hello Rola!' in response.content.decode()

@pytest.mark.django_db
def test_signup_view(client):
    response = client.get(reverse('signup'))
    assert response.status_code == 200
    assert 'myapp/signup.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_login_view(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200
    assert 'myapp/login.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_api_view_get(client, user):
    client.login(username='testuser', password='complex_password123')
    response = client.get(reverse('myapp:myapp'))
    assert response.status_code == 200
    assert 'myapp/formulaire.html' in [t.name for t in response.templates]

@patch('requests.get')
@pytest.mark.django_db
def test_api_view_post(mock_get, client, user):
    client.login(username='testuser', password='complex_password123')
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.text = '{"faces":[{"bbox":[139.29549071043752,185.8942106522123,211.2634360686308,278.7116930608726],"score":0.9936680197715759,"age":39.74738493585028,"class":"Age - Adult"},{"bbox":[371.91275590162337,65.29337760344863,448.1290859205329,161.90829295588202],"score":0.9898697733879089,"age":69.0,"class":"Age - Senior Adult"}],"status":"ok"}'

    response = client.post(reverse('myapp:myapp'), {'image_url': 'http://example.com/image.jpg'})
    assert response.status_code == 200
    assert 'Age - Adult' in response.content.decode()
    assert 'Age - Senior Adult' in response.content.decode()

# Models Tests:
@pytest.mark.django_db
def test_image_prediction_model():
    prediction_data = {
        'faces': [
            {
                'bbox': [139.29549071043752, 185.8942106522123, 211.2634360686308, 278.7116930608726],
                'score': 0.9936680197715759,
                'age': 39.74738493585028,
                'class': 'Age - Adult'
            },
            {
                'bbox': [371.91275590162337, 65.29337760344863, 448.1290859205329, 161.90829295588202],
                'score': 0.9898697733879089,
                'age': 69.0,
                'class': 'Age - Senior Adult'
            }
        ],
        'status': 'ok'
    }
    prediction = ImagePrediction.objects.create(
        image_url='http://example.com/image.jpg',
        prediction_data=prediction_data
    )
    expected_string = ("Image URL: http://example.com/image.jpg - Predictions: "
                       "{'faces': [{'bbox': [139.29549071043752, 185.8942106522123, 211.2634360686308, "
                       "278.7116930608726], 'score': 0.9936680197715759, 'age': 39.74738493585028, 'class': 'Age - Adult'}, "
                       "{'bbox': [371.91275590162337, 65.29337760344863, 448.1290859205329, 161.90829295588202], "
                       "'score': 0.9898697733879089, 'age': 69.0, 'class': 'Age - Senior Adult'}], 'status': 'ok'}")

    assert str(prediction) == expected_string

#----------------------------------------------------------

# import pytest
# from django.urls import reverse
# from django.contrib.auth.models import User
# from django.test import Client
# from myapp.models import ImagePrediction
# # from django.utils import timezone
# import json

# @pytest.mark.django_db
# def test_hello_view():
#     client = Client()
#     response = client.get(reverse('hello'))
#     assert response.status_code == 200
#     assert "Hello Rola!" in response.content.decode()

# @pytest.mark.django_db
# def test_signup_view():
#     client = Client()
#     response = client.post(reverse('signup'), {
#         'username': 'testuser',
#         'password1': 'testpassword123',
#         'password2': 'testpassword123'
#     })
#     assert response.status_code == 302  # Redirect after successful signup
#     assert User.objects.filter(username='testuser').exists()

# @pytest.mark.django_db
# def test_login_user_view():
#     user = User.objects.create_user(username='testuser', password='testpassword123')
#     client = Client()
#     response = client.post(reverse('login'), {
#         'username': 'testuser',
#         'password': 'testpassword123'
#     })
#     assert response.status_code == 302  # Redirect after successful login
#     assert response.url == reverse('home')

# @pytest.mark.django_db
# def test_logout_user_view():
#     user = User.objects.create_user(username='testuser', password='testpassword123')
#     client = Client()
#     client.login(username='testuser', password='testpassword123')
#     response = client.get(reverse('logout'))
#     assert response.status_code == 302  # Redirect after logout
#     assert response.url == reverse('login')

# @pytest.mark.django_db
# def test_api_view(mocker):
#     client = Client()
#     user = User.objects.create_user(username='testuser', password='testpassword123')
#     client.login(username='testuser', password='testpassword123')

#     mock_response = mocker.patch('requests.get')
#     mock_response.return_value.status_code = 200
#     mock_response.return_value.text = json.dumps({
#         'faces': [{'age': 25, 'gender': 'male'}]
#     })

#     response = client.post(reverse('myapp:myapp'), {
#         'image_url': 'https://example.com/image.jpg'
#     })

#     assert response.status_code == 200
#     assert 'faces' in response.content.decode()
#     assert ImagePrediction.objects.count() == 1

#     prediction_instance = ImagePrediction.objects.first()
#     assert prediction_instance.image_url == 'https://example.com/image.jpg'
#     assert json.loads(prediction_instance.prediction_data) == [{'age': 25, 'gender': 'male'}]








# # import pytest
# # from django.urls import reverse
# # from django.contrib.auth.models import User
# # from myapp.forms import SignupForm  # Import your custom SignupForm
# # from django.contrib.auth.forms import UserCreationForm

# # @pytest.mark.django_db
# # def test_homepage(client):
# #     # Test homepage view for authenticated user
# #     user = User.objects.create_user(username='testuser', password='12345')
# #     client.login(username='testuser', password='12345')
# #     response = client.get(reverse('home'))
# #     assert response.status_code == 200
    
# # @pytest.mark.django_db
# # def test_homepage_unauthenticated(client):
# #     # Test homepage view for unauthenticated user
# #     response = client.get(reverse('home'))
# #     assert response.status_code == 302  # Redirects to login page
    
# # @pytest.mark.django_db
# # def test_signup(client):
# #     # Test signup view
# #     response = client.get(reverse('signup'))
# #     assert response.status_code == 200
# #     # Check if the form is an instance of UserCreationForm or SignupForm
# #     assert isinstance(response.context['form'], UserCreationForm)

# # @pytest.mark.django_db
# # def test_login_user(client):
# #     # Test login view with valid credentials
# #     user = User.objects.create_user(username='Dr.Django', password='passworddjango')
# #     response = client.get(reverse('login'))
# #     assert response.status_code == 200

# # @pytest.mark.django_db
# # def test_logout_user(client):
# #     # Test logout view
# #     user = User.objects.create_user(username='testuser', password='12345')
# #     client.login(username='testuser', password='12345')
# #     response = client.get(reverse('logout'))
# #     assert response.status_code == 302  # Redirects to login page

# # # This test requires the pytest-mock fixture to be available
# # @pytest.mark.django_db
# # def test_api(client, mocker):
# #     # Test API view
# #     # Mock requests.get to avoid making actual API calls during tests
# #     mocker.patch('requests.get')
# #     # You can add your API test logic here
# #     pass
