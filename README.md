Working Time Analysis - Portfolio Project

A portfolio project for analyzing working hours using Python, IaC, and DaC.

Current Status: Version 1.5

The core logic of the analysis tool has been significantly refactored. The application now:

    Calculates worked hours dynamically from start and end times.

    Runs as a persistent, interactive service within its container.

    Correctly separates the logic for daily 10h+ violations from the cumulative monthly overtime/undertime balance.

    Implements professional logging to a persistent file for monitoring and debugging, separate from the user report.

    Prints a detailed, user-facing summary report to the console.

Infrastructure (Terraform): The Terraform configuration now successfully builds the Python application's Docker image and runs it as a container. A persistent volume is correctly mounted to store log files on the host system.

For more details on the Python application, see the Python-App/README.md.

Project Vision / Roadmap

This project will be developed iteratively. Future steps include:

    [ ] Phase 2: Storing and retrieving data from a database.

    [In Progress] Phase 3: Containerizing the Python application and the database using Docker. (The Python application is now fully containerized; the database is next).

    [In Progress] Phase 4: Defining the required infrastructure as code (IaC) using Terraform. (The IaC for the application container is complete; the database infrastructure is next).

    [ ] Phase 5: Managing the application and infrastructure with configuration management tools like Ansible.

Technologies

    Python 3

    Terraform

    Docker
