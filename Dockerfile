# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . .

# Install the application dependencies
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Set the entrypoint command to run the Flask application
CMD ["python", "main.py"]
