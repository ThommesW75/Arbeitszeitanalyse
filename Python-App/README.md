Python Application: Working Time Analysis

This directory contains the Python script for the core application logic.

Current Version: 1.4

Features

    Calculates worked hours dynamically based on start and end times.

    Analyzes data from a flexible, in-script data source designed to be easily replaced by a database.

    Categorizes employees based on their working hours (overtime, undertime, 10h+ violations).

    Prints a summary report to the console.

    Code is structured with separate functions for data loading and calculation for better maintainability.

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

Navigate to the main project directory (Arbeitszeitanalyse). Execute the script using the following command:
Bash

python3 Python-App/Arbeitszeitanalyse.py
