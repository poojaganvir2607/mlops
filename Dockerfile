# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only code + requirements
COPY anomaly_project/ ./anomaly_project
COPY anomaly_project/requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Create empty folders for runtime outputs
RUN mkdir -p data models

# Default command
CMD ["python", "anomaly_project/anomaly.py"]

