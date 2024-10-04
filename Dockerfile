# Use an official Python runtime as a parent image
FROM python:3.10-slim
# FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY myproject/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r myproject/requirements.txt

# Copy your Django project into the container
# COPY . /app/
COPY myproject /app/myproject

# Copy .env file into the container
 COPY .env /app/.env

# Collect static files (if necessary)
# RUN python manage.py collectstatic --noinput

# Set the PYTHONPATH to include the nested myproject
ENV PYTHONPATH /app/myproject

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Gunicorn (production)
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

# Run Django's development server (useful for local development or debugging)
# CMD ["python3", "/app/myproject/manage.py", "runserver", "0.0.0.0:8000"]

# Check Gunicorn Logs
# CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:8000", "--log-level", "debug", "myproject.wsgi:application"]

# Run Gunicorn (production)
# CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

# Existing CMD line in your Dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]




# Delete local docker containers
# Add User to Docker Group
# sudo usermod -aG docker utilisateur (username)

# verify that utilisateur is in the docker group:
    # groups

# Log out the login
# newgrp docker

# Restart Docker service
# sudo systemctl restart docker

# stop and delete all local containers
# docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)










# # Use an official Python runtime as a parent image
# FROM python:3.10-slim

# # # Set environment variables
# # ENV PYTHONUNBUFFERED 1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY /myproject/requirements.txt /app/

# # Copy .env file into the container
# COPY .env /app/.env


# # Install any needed packages specified in requirements.txt
# RUN python -m pip install --no-cache-dir --upgrade  -r /app/requirements.txt 

# # # Copy the current directory contents into the container at /app
# # COPY . /app/
# # Copy the entire Django project into the container
# COPY myproject /app/myproject

# # Set environment variables
# ENV PYTHONPATH=/app/myproject

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run the application
# # CMD ["python", "/app/myproject/manage.py", "runserver", "0.0.0.0:8000","--noreload"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]







# # # Use an official Python runtime as a parent image
# # FROM python:3.10-slim

# # # Set the working directory in the container
# # WORKDIR /app

# # # Copy the requirements file into the container at /app
# # COPY myproject/requirements.txt /app/

# # # Copy the current directory contents into the container at /app
# #  COPY . /app

# # # Copy .env file into the container
# #  COPY .env /app/.env

# # # Install any needed packages specified in requirements.txt
# # RUN python -m pip install --no-cache-dir --upgrade -r /app/requirements.txt 

# # # Copy the entire Django project into the container at /app/myproject
# # COPY myproject /app/myproject

# # # Set environment variables
# # ENV PYTHONPATH=/app/myproject

# # ENV DJANGO_SETTINGS_MODULE=myproject.settings  
# # # Update this to your actual settings path

# # # Create the directory for Gunicorn logs
# # # RUN mkdir -p /var/log/gunicorn

# # # Make port 8000 available to the world outside this container
# # EXPOSE 8000

# # # Run the application with Gunicorn
# # CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
# # # CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application", "--log-level", "info", "--access-logfile", "/var/log/gunicorn/access.log", "--error-logfile", "/var/log/gunicorn/error.log"]








