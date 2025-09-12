# Use a lightweight Python base image as a foundation.
FROM python:3.9-slim

# Set the working directory inside the image.
WORKDIR /app

# Copy the entire Python-App directory into the container.
COPY ./Python-App/ .

# This command runs your application when the container starts.
# It now uses a single, consistent file name.
# This command just keeps the container running and waiting for exec commands.
CMD ["tail", "-f", "/dev/null"]