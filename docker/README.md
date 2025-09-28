# Database Service

This directory contains all files needed to build the database container for the time tracking application.

## Purpose

The goal is to create a self-contained MariaDB container that automatically manages its database schema using Flyway. This approach is called "Database as Code".

## Contents

- **`Dockerfile`**: The blueprint for building our custom Docker image. It starts with the official MariaDB image and adds the Flyway command-line tool.

- **`entrypoint.sh`**: A custom startup script for the container. It waits for the database to be ready and then runs `flyway migrate` to apply any new SQL scripts before the database accepts connections.

- **`sql/`**: This directory holds all versioned SQL migration scripts. Flyway executes these scripts in order to build or update the database schema.
  - `V1__Initiales_Schema.sql`: The first script that creates the initial tables.
