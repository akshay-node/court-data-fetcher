# Base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all project files
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Default command to run app
CMD ["python", "app.py"]
