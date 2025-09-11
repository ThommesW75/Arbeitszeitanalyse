Python Application: Working Time Analysis

This directory contains the Python script for the core application logic.

Current Version: 1.5

Features

    Calculates worked hours dynamically based on start and end times.

    Analyzes data from a flexible, in-script data source.

    Categorizes employees for 10h+ violations and overtime/undertime.

    Runs as a persistent, interactive service that can be re-triggered without restarting.

    Logs technical events (start, finish, errors) to both the console and a persistent file for easy monitoring.

    Prints a clean, user-facing summary report to the console, separate from technical logs.

Changes in v1.5

    Service-Oriented Architecture: The script has been refactored to run as a persistent service instead of a one-shot execution. A main while loop was added to keep the application alive and allow for interactive re-analysis, making it suitable for containerized operation.

    Professional Logging: Implemented a robust logging system using Python's built-in logging module. Technical status messages are now logged with timestamps and levels to both the console (for docker logs) and a persistent file, separating them cleanly from the user-facing report.

    Code Modularization: The core analysis logic was moved into a dedicated run_analysis() function to improve code structure and readability within the new main loop.

Changes in v1.4

    Decoupled Analysis Logic: The core analysis logic was refactored. The previous if/elif/elif structure was replaced with two independent checks. This ensures that 10h+ violations are now also correctly registered as overtime.

    Advanced Violation Reporting: Implemented a more sophisticated data collection for 10h+ violations using a dictionary. The final report now shows a detailed summary per employee, including the number of violations and the specific dates on which they occurred.

    Improved User Output: Refined the wording in the report for better readability and user experience.

Changes in v1.3

    Major Data Refactoring: The static data source ('stunden') has been replaced with a dynamic structure using 'start_time', 'end_time', and 'contract_hours'. The data list has been moved into a dedicated load_time_tracking_data() function to cleanly separate data from logic.

    Dynamic Calculation: A new calculate_hours() function was introduced. The application no longer reads static hours but calculates them dynamically, making the system flexible and realistic.

    Code Standardization: All function names and dictionary keys have been refactored to use a consistent English naming convention (e.g., calculate_hours, contract_hours), following professional development standards.

Changes in v1.2

    Refactoring: The entire script logic was moved into a main() function and is now started by a standard if __name__ == "__main__": block. This improves the structure and prepares the code for future extensions and modularization.

Changes in v1.1

    Refactoring: Replaced hardcoded "magic numbers" (like 10, 9, 8) for business rules with configuration variables at the top of the script. This makes the code more readable and easier to maintain.

How to Run

Locally

Navigate to the main project directory and execute the script:
Bash

python3 Python-App/Arbeitszeitanalyse.py

In Docker (Recommended Workflow)

    Start the container:
    Bash

terraform apply

Interact with the application:
Bash

docker attach arbeitszeitanalyse

Once attached, press Enter to run an analysis or type q and then Enter to quit the application.

View technical logs:
Bash

docker logs arbeitszeitanalyse

The persistent log file (Arbeitszeitanalyse.log) will be available on the host machine in the directory specified in your Terraform variables.
