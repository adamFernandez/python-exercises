# Use an official Python image as the base image
FROM python:3.8-slim

RUN useradd --create-home --shell /bin/bash app_user

# Set the working directory inside the container
WORKDIR /home/app_user

# Copy your Python code into the container
COPY requirements.txt ./

# Install any required dependencies (replace with your requirements file if applicable)
RUN apt-get -y update && apt-get install -y sqlite3
RUN pip install --no-cache-dir -r requirements.txt

USER app_user

COPY . .

# Command to run your Python script (replace with your script's name)
CMD ["bash"]