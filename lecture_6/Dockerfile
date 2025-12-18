FROM python:3.11-slim

# Set working directory inside the container.

WORKDIR /app


# Copy requirements file for this service.

COPY requirements.txt .

# Install dependencies.

RUN pip install --no-cache-dir -r requirements.txt


# Copy application source code.

COPY main.py .


# Expose port for FastAPI.

EXPOSE 8000


# Run FastAPI application.

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
