# Use the official Python image as the base
FROM python:3.12-slim

# Set up working directory
WORKDIR /app

# Copy your application files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

