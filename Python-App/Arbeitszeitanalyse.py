#!/usr/bin/env python3
# This "Shebang" allows the script to be executed directly on Linux systems
# after setting the correct permissions (chmod +x).

from datetime import datetime, timedelta # We need these tools for time calculations.
import logging
import os

# --- GLOBAL CONSTANTS / CONFIGURATION ---
MAX_WORK_HOURS = 10.0  # Maximum allowed working hours per day.
LOG_FILE_PATH = "logs/Arbeitszeitanalyse.log" 

def setup_logging():
    """
    Configures the logging system to write to a file.
    """
    # Get the root logger object
    logger = logging.getLogger()
    logger.setLevel(logging.INFO) # Set the lowest level of messages to log

    # --- Create a file handler to write logs to a file ---
    log_directory = os.path.dirname(LOG_FILE_PATH)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Now, create the handler that writes to our file.
    file_handler = logging.FileHandler(LOG_FILE_PATH)

    # Define the format for the log messages.
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Tell the file handler to use this format.
    file_handler.setFormatter(formatter)

    # Finally, add the new handler to our logger.
    logger.addHandler(file_handler)

    # Also add a handler to log to the console (for docker logs)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter) # We use the same format as for the file
    logger.addHandler(stream_handler)


# =================================================================
# --- DATA SOURCE FUNCTION (Phase 1.1 - Complete & Refactored) ---
# =================================================================
def load_time_tracking_data():
    """
    This function holds and returns our complete list of time tracking data.
    The data structure now uses a consistent English naming convention and includes a date.
    """
    time_tracking_data = [
        {'name': 'Wolfgang Klein', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Julia Wagner', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Holger Frank', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '09:00', 'end_time': '17:00'},
        {'name': 'Lukas Müller', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '07:30', 'end_time': '18:00'},
        {'name': 'Jörg Bauer', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '15:30'},
        {'name': 'Werner Vogel', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Michael Becker', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Monika Wolf', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Sabine Schulz', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Claudia Adler', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Klaus Schäfer', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Bernd Neumann', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Peter Schmidt', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '18:00'},
        {'name': 'Heike Schwarz', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Andreas Hoffmann', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Dieter Zimmermann', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Petra Richter', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '09:00', 'end_time': '16:00'},
        {'name': 'Susanne Koch', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Ursula Krüger', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Hanna Schmitt', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Thomas Fischer', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Kristina Meier', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Lennart Weber', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Karl Braun', 'contract_hours': 8.0, 'date': '2025-09-08', 'start_time': '08:00', 'end_time': '16:00'},
    ]
    return time_tracking_data

# =================================================================
# --- CALCULATION FUNCTION (Phase 1.2) ---
# =================================================================
def calculate_hours(start_time_str, end_time_str):
    """
    This function calculates the total hours between a start and end time.
    It takes two texts and returns one number.
    """
    time_format = '%H:%M'
    start_time = datetime.strptime(start_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)
    duration = end_time - start_time
    total_hours = duration.total_seconds() / 3600
    return total_hours

# =================================================================
# --- MAIN PROGRAM (v1.2 Logic with new Data Source) ---
# =================================================================
def main():
    """
    Analyzes the employee time tracking data and prints a report.
    This version uses the original logic but with the new data structure.
    """
    # Call the setup function right at the very start!
    setup_logging()

    # Log entry for the program start
    logging.info("Starting analysis...")
    
    # --- DATA SOURCE ---
    # We load the data from our new function.
    all_data = load_time_tracking_data()
    # Log entry after loading data
    logging.info(f"Successfully loaded {len(all_data)} records.")

    # --- Step 2: Prepare containers for the analysis results ---
    ten_hour_violations = {}
    overtime_employees = []
    undertime_employees = []
    
    # We don't need the counters anymore, we can get the number from the list length.

    # --- Step 3: Analyze the data (adapted logic) ---
    # We loop through the list of employees one by one.
    for employee_record in all_data:
        # Get the data for the current employee.
        name = employee_record['name']
        contract_hours = employee_record['contract_hours']
        start_time = employee_record['start_time']
        end_time = employee_record['end_time']
        date = employee_record['date']

        # THIS IS THE KEY CHANGE:
        # Instead of reading the hours, we now calculate them.
        worked_hours = calculate_hours(start_time, end_time)

        # Part A: Check for 10-hour violations (independent check)
        if worked_hours >= MAX_WORK_HOURS:
            if name not in ten_hour_violations:
                ten_hour_violations[name] = [date]
            else:
                ten_hour_violations[name].append(date)

        # Part B: Check for overtime or undertime (independent check)
        # We calculate the balance for this single day.
        daily_balance = worked_hours - contract_hours

        if daily_balance > 0:
            overtime_employees.append(name)
        elif daily_balance < 0:
            undertime_employees.append(name)
       
       

    # --- Step 4: Print the results ---
    print("--- Analyse der Arbeitszeiten ---")

    # --- Part A: Report for 10-Hour Violations ---
    print(f"\n--- Auswertung: 10-Stunden-Verstöße ---")

    # We loop through our collected violations dictionary.
    for name, dates in ten_hour_violations.items():
        # Get the number of violations from the length of the list.
        violation_count = len(dates)
        
        # Create the final output string using an f-string with curly braces {}.
        print(f"Mitarbeiter {name} hat {violation_count} mal länger als 10 Stunden gearbeitet an den Tagen: {dates}")

    # --- Part B: Report for Overtime and Undertime ---
    # This part uses the simple lists, just like in your v1.2
    print(f"\n--- Auswertung: Über- und Minusstunden ---")
    print(f"INFO: {len(overtime_employees)} Mitarbeiter haben Überstunden geleistet.")
    print(f"Namen: {overtime_employees}")

    print(f"\nHINWEIS: {len(undertime_employees)} Mitarbeiter haben Minusstunden gemacht.")
    print(f"Namen: {undertime_employees}")

    print("\n--- Analyse abgeschlossen ---")
    # The final technical message is now a log entry.
    logging.info("Analysis finished.")

# This is the standard way to start a Python program.
# The code inside this if-block only runs when the script is executed directly.
if __name__ == "__main__":
    main()
