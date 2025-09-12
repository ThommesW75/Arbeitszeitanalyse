# Launcher Script: start-analyse.sh

This script is the primary entry point for users to interact with the Working Time Analysis application.

## Purpose

The `start-analyse.sh` script starts a new, interactive session with the Python application inside the already running Docker service container.

## Prerequisites

Before running this script, ensure the following conditions are met:

1.  **Docker is installed and the Docker daemon is running.**
2.  The application's Docker image (`arbeitszeitanalyse:latest`) has been built.
3.  The application's service container (`arbeitszeitanalyse`) is running in the background.

Both the image and the service container are managed via Terraform. To ensure everything is set up correctly, run the following command in the `terraform/app` directory:

```bash
terraform apply
