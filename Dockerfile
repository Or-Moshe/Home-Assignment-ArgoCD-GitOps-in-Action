# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

# Command to run the app
CMD ["python", "app.py"]