<<<<<<< HEAD
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
=======
# Use the official MySQL image from the Docker Hub
FROM mysql:latest

# Set the environment variables
ENV MYSQL_ROOT_PASSWORD=sachin
ENV MYSQL_DATABASE=cafe
ENV MYSQL_USER=liya
ENV MYSQL_PASSWORD=greeshma

# Copy the SQL script to initialize the database
COPY init.sql /docker-entrypoint-initdb.d/
>>>>>>> 4541826b16ee58ac49e1c8f6e587c4908c1d0105
