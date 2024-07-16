# Stage 1: Build stage for city_server.py
FROM python:3.9-slim AS city_server

WORKDIR /app

# Install dependencies for city_server.py
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy city_server.py and any other necessary files
COPY city_server.py .

# Expose port for Flask application
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "city_server.py"]

# Stage 2: Build stage for client.py
FROM python:3.9-slim AS client

WORKDIR /app

# Copy client.py and any dependencies (if any)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY client.py .

# Command to run the client script
CMD ["python", "client.py"] 