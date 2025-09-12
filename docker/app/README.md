# Docker App Container

This directory contains the files needed to build the Docker image for the main application.

## Purpose

The `Dockerfile` defines the steps to create a self-contained and portable image for the application. The process includes:

1.  Starting from a lightweight, official Python base image (`python:3.11-slim`).
2.  Setting up a working directory within the image (`/app`).
3.  Copying the application source code (`Arbeitszeitanalyse.py`) into the image.
4.  Setting the default startup command to `tail -f /dev/null`. This turns a container created from this image into a **persistent, non-interactive background service** that waits for commands, rather than a script that runs once and exits.

## Image Build and Usage

### Building the Image (Managed by Terraform)

**The Docker image should not be built manually.** The build process is defined and managed as part of the Infrastructure as Code (IaC) workflow.

To build or update the image, navigate to the Terraform directory and run `apply`:
```bash
cd ../../terraform/app
terraform apply
