# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose the port your app runs on
EXPOSE 80

# Start the app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]

