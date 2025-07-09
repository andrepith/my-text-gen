# Use an official lightweight Python image
FROM python:3.10-slim

# System dependencies for Torch, Transformers, etc.
RUN apt-get update && apt-get install -y \
    git \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Expose FastAPI app
EXPOSE 7860

# Run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
