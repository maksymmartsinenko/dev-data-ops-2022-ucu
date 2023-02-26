# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Create a non-root user and group to run the application
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set the working directory for the application
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the user to the non-root user created earlier
USER appuser

# Set the environment variable for the MongoDB URI
ENV MONGO_URI mongodb://mongo:27017/

# Set the command to run when the container starts
CMD ["python", "main.py", "--host=0.0.0.0", "--port=80"]

