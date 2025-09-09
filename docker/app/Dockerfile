# Use a lightweight Python base image as a foundation.
FROM python:3.9-slim

# Set the working directory inside the image.
WORKDIR /app

# Copy the application file into the image.
# The path is now relative to the root of your project.
COPY ./Python-App/Arbeitszeitanalyse_v1.4.py /app/

# This command runs your application when the container starts.
CMD ["python", "Arbeitszeitanalyse_v1.4.py"]