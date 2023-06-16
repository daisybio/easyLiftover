# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for Django
ENV DJANGO_SETTINGS_MODULE=webuplift.settings

# Set command to run when running the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
