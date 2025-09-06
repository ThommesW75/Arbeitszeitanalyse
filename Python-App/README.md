Python Application: Working Time Analysis

This directory contains the Python script for the core application logic.

Current Version: 1.2
Features

    Analyzes a hardcoded list of employee data (name and hours).

    Categorizes employees based on their working hours (overtime, undertime, etc.).

    Prints a summary report to the console.

    The code is structured in a main function for clarity and future expansion.

    
    Changes in v1.2

    Refactoring: The entire script logic was moved into a main() function and is now started by a standard if __name__ == "__main__": block. This improves the structure and prepares the code for future extensions and modularization.

    Changes in v1.1

    Refactoring: Replaced hardcoded "magic numbers" (like 10, 9, 8) for business rules with configuration variables at the top of the script. This makes the code more readable and easier to maintain.

How to Run

    Navigate to the main project directory (Arbeitszeitanalyse).

    Execute the script using the following command:

    python3 Python-App/zeiterfassung_v1.1.py
