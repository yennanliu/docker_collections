# Base image with Python 3.9
FROM python:3.9-slim

# Set environment variables for Flask app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Install dependencies
RUN pip install --upgrade pip
RUN pip install Flask prometheus_client

# Add the Flask app code
COPY app.py /app.py

# Expose necessary ports (Flask app on 5000, Prometheus metrics on 8000)
EXPOSE 5000
EXPOSE 8000

# Command to run the Flask app
CMD ["flask", "run"]