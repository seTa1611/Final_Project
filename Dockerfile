# Dockerfile for FastAPI ToDo App
# Using official Python slim image - keeps things small

FROM python:3.13.6-slim

WORKDIR /app

# Install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code over
COPY . .

# Run the server (listens on port 80 inside container)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]