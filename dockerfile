# Use the official Python base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"


# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies
RUN apt-get update && apt-get install -y git ffmpeg && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

ENV LISTEN_PORT=5000

# Expose the port that the app will run on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "5000"]
