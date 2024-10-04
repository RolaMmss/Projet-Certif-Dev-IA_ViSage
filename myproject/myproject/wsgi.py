# """
# WSGI config for myproject project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# application = get_wsgi_application()




# In your wsgi.py or asgi.py file
import os
import sys

# Add the path to your project if needed
sys.path.append('../myproject/myproject/')

# Initialize OpenTelemetry setup
from .opentelemetry_setup import *  # Import your setup script here

# Standard Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
