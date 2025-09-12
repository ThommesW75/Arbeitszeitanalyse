#!/usr/bin/env python3
# This "Shebang" allows the script to be executed directly on Linux systems.

from datetime import datetime, timedelta
import logging
import os
import time

# =================================================================
# --- CONFIGURATION ---
# =================================================================
MAX_WORK_HOURS = 10.0
LOG_FILE_PATH = "logs/Arbeitszeitanalyse.log" # Path for the log file

# =================================================================
# --- LOGGING SETUP ---
# =================================================================
def setup_logging():
    """
    Configures the logging system to write to a file and the console.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create the log directory if it doesn't exist
    log_directory = os.path.dirname(LOG_FILE_PATH)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Create a handler to write to the file
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    
# =================================================================
# --- DATA SOURCE FUNCTION ---
# =================================================================
def load_time_tracking_data():
    """
    This function holds and returns our complete list of time tracking data.
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
# --- CALCULATION FUNCTION ---
# =================================================================
def calculate_hours(start_time_str, end_time_str):
    """
    This function calculates the total hours between a start and end time.
    """
    time_format = '%H:%M'
    start_time = datetime.strptime(start_time_str, time_format)
    end_time = datetime.strptime(end_time_str, time_format)
    duration = end_time - start_time
    total_hours = duration.total_seconds() / 3600
    return total_hours

# =================================================================
# --- ANALYSIS FUNCTION ---
# =================================================================
def run_analysis():
    """
    This function contains the core logic for a single analysis run,
    including the final report printing.
    """
    logging.info("Loading data for analysis run...")
    all_data = load_time_tracking_data()
    logging.info(f"Successfully loaded {len(all_data)} records.")

    # Prepare containers for results
    ten_hour_violations = {}
    overtime_employees = []
    undertime_employees = []

    logging.info("Starting analysis loop...")
    for employee_record in all_data:
        name = employee_record['name']
        contract_hours = employee_record['contract_hours']
        start_time = employee_record['start_time']
        end_time = employee_record['end_time']
        date = employee_record['date']
        
        worked_hours = calculate_hours(start_time, end_time)

        # Part A: Check for 10-hour violations (independent check)
        if worked_hours >= MAX_WORK_HOURS:
            if name not in ten_hour_violations:
                ten_hour_violations[name] = [date]
            else:
                ten_hour_violations[name].append(date)

        # Part B: Check for overtime or undertime (independent check)
        daily_balance = worked_hours - contract_hours
        if daily_balance > 0:
            overtime_employees.append(name)
        elif daily_balance < 0:
            undertime_employees.append(name)
    
    logging.info("Analysis loop finished.")

    # --- Print the results for the user ---
    print("\n--- Analyse der Arbeitszeiten ---")
    print(f"\n--- Auswertung: 10-Stunden-Verstöße ---")
    for name, dates in ten_hour_violations.items():
        violation_count = len(dates)
        print(f"Mitarbeiter {name} hat {violation_count} mal länger als 10 Stunden gearbeitet an den Tagen: {dates}")

    print(f"\n--- Auswertung: Über- und Minusstunden ---")
    print(f"INFO: {len(overtime_employees)} Mitarbeiter haben Überstunden geleistet.")
    print(f"Namen: {overtime_employees}")
    print(f"\nHINWEIS: {len(undertime_employees)} Mitarbeiter haben Minusstunden gemacht.")
    print(f"Namen: {undertime_employees}")
    print("\n--- Analyse für diesen Durchlauf abgeschlossen ---\n")
    logging.info("Report printed to console.")


# =================================================================
# --- MAIN PROGRAM with Loop ---
# =================================================================
def main():
    """
    Main control function with an interactive menu loop.
    """
    setup_logging()
    logging.info("Application started successfully. Ready for user input.")

    
    while True:
        # The menu is now part of the input prompt itself.
        menu_text = (
            "\n--- Hauptmenü ---\n"
            "1: Komplette Monatsanalyse durchführen\n"
            "q: Programm beenden\n"
            "Bitte wähle eine Option und drücke Enter: "
        )
        choice = input(menu_text)
        
        if choice == '1':
            run_analysis()
        elif choice.lower() == 'q':
            logging.info("User requested to quit. Shutting down.")
            break
        else:
            print("\nUngültige Eingabe, bitte versuche es erneut.")
            time.sleep(1)

# =================================================================
# --- SCRIPT START ---
# =================================================================
if __name__ == "__main__":
    main()
