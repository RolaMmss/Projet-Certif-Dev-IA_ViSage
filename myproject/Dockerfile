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
