# Docker App Container

This directory contains the files needed to build the Docker image for the main application.

## Purpose

The **Dockerfile** is a build script that creates a self-contained image. This image includes the Python interpreter and the application files. This makes the application portable and easy to run in any environment (e.g., on your local PC or in the cloud).

## Usage

To build the Docker image, run the following command from this directory:

```bash
docker build -t arbeitszeitanalyse:latest .
