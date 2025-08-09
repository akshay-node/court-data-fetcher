# Base image
FROM python:3.10-slim

# Update apt and install sqlite3 and its dev libraries
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev



# Set working directory inside container
WORKDIR /app

# Copy all project files
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run init_db.py pehle phir app.py
CMD python init_db.py && python app.py
