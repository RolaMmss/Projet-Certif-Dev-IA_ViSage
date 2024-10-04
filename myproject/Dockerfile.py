# # Use an official Python runtime as a parent image
# FROM python:3.12-slim
# # FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set work directory
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends gcc \
#     && rm -rf /var/lib/apt/lists/*

# # Install Python dependencies
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir --upgrade pip \
#     && pip install --no-cache-dir -r requirements.txt

# # Copy your Django project into the container
# COPY . /app/

# # Collect static files (if necessary)
# RUN python manage.py collectstatic --noinput

# # Run Gunicorn
# CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]






# # Use an official Python runtime as a parent image
# FROM python:3.10-slim
# # FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set work directory
# WORKDIR /app

# RUN mkdir /app/app_web

# # # Install system dependencies
# # RUN apt-get update \
# #     && apt-get install -y --no-install-recommends gcc \
# #     && rm -rf /var/lib/apt/lists/*

# # Install Python dependencies
# COPY ./requirements.txt /app/app_web/requirements.txt

# # # Install any needed packages specified in requirements.txt
# # RUN pip install --no-cache-dir --upgrade pip \
# #     && pip install --no-cache-dir -r requirements.txt
# RUN python -m pip install --no-cache-dir --upgrade  -r /app/myproject/requirements.txt

# # Copy your Django project into the container
# # COPY . /app/
# COPY . /app/myproject

# # Collect static files (if necessary)
# RUN python manage.py collectstatic --noinput

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# WORKDIR /app/app_web
# # Run Gunicorn (production)
# # CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

# # Run Django's development server (useful for local development or debugging)
# CMD ["python3", "/app/myproject/manage.py", "runserver", "0.0.0.0:8000"]

# # Check Gunicorn Logs
# # CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:8000", "--log-level", "debug", "myproject.wsgi:application"]













# # Use an official Python runtime as a parent image
# FROM python:3.10-slim
# # FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set work directory
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends gcc \
#     && rm -rf /var/lib/apt/lists/*

# # Install Python dependencies
# COPY myproject/requirements.txt /app/

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir --upgrade pip \
#     && pip install --no-cache-dir -r requirements.txt

# # Copy your Django project into the container
# # COPY . /app/
# COPY myproject /app/myproject

# # Copy .env from the parent directory into the container
# COPY myproject/.env /app/.env

# # Collect static files (if necessary)
# # RUN python manage.py collectstatic --noinput

# # Set the PYTHONPATH to include the nested myproject
# ENV PYTHONPATH /app/myproject

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Existing CMD line in your Dockerfile
# # CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
# CMD ["python", "myproject/manage.py", "runserver", "0.0.0.0:8000"]









# Use an official Python runtime as a parent image
FROM python:3.10-slim

# # Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Copy .env file into the container
COPY .env /app/.env


# Install any needed packages specified in requirements.txt
RUN python -m pip install --no-cache-dir --upgrade  -r /app/requirements.txt 

# # Copy the current directory contents into the container at /app
# COPY . /app/
# Copy the entire Django project into the container
COPY myproject /app/myproject

# Set environment variables
ENV PYTHONPATH=/app/myproject

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000","--noreload"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
# CMD ["gunicorn", "--bind", ":8000", "--chdir", "/app/myproject", "myproject.wsgi:application"]