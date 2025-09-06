# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY anomaly_project/ ./anomaly_project
COPY data/ ./data
COPY models/ ./models
COPY anomaly_project/requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command to run
CMD ["python", "anomaly_project/anomaly.py"]

