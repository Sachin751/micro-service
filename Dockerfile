# Use the official MySQL image from the Docker Hub
FROM mysql:latest

# Set the environment variables
ENV MYSQL_ROOT_PASSWORD=sachin
ENV MYSQL_DATABASE=cafe
ENV MYSQL_USER=liya
ENV MYSQL_PASSWORD=greeshma

# Copy the SQL script to initialize the database
COPY init.sql /docker-entrypoint-initdb.d/
