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
# RUN python3 -m pip install --no-cache-dir --upgrade  -r /app/requirements.txt 

# # # Copy the current directory contents into the container at /app
# # COPY . /app/
# # Copy the entire Django project into the container
# COPY myproject /app/myproject

# # Set environment variables
# ENV PYTHONPATH=/app/myproject

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run the application
# CMD ["python3", "/app/myproject/manage.py", "runserver", "0.0.0.0:8000"]






# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY myproject/requirements.txt /app/

# Copy the current directory contents into the container at /app
 COPY . /app

# Copy .env file into the container
 COPY .env /app/.env

# Install any needed packages specified in requirements.txt
RUN python -m pip install --no-cache-dir --upgrade -r /app/requirements.txt 

# Copy the entire Django project into the container at /app/myproject
COPY myproject /app/myproject

# Set environment variables
ENV PYTHONPATH=/app/myproject

ENV DJANGO_SETTINGS_MODULE=myproject.settings  
# Update this to your actual settings path

# Create the directory for Gunicorn logs
# RUN mkdir -p /var/log/gunicorn

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application", "--log-level", "info", "--access-logfile", "/var/log/gunicorn/access.log", "--error-logfile", "/var/log/gunicorn/error.log"]