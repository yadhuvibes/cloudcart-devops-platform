# Base Image
FROM python:3.11-slim

# Maintainer
LABEL maintainer="Yadhukrishna PR"

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python output immediately
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy dependency file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Flask Port
EXPOSE 5000

# Start application
CMD ["python", "app.py"]
