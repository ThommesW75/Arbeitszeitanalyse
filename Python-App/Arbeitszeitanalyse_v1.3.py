#!/usr/bin/env python3
# This "Shebang" allows the script to be executed directly on Linux systems
# after setting the correct permissions (chmod +x).

from datetime import datetime, timedelta # We need these tools for time calculations.

# =================================================================
# --- DATA SOURCE FUNCTION (Phase 1.1 - Complete & Refactored) ---
# =================================================================
def load_time_tracking_data():
    """
    This function holds and returns our complete list of time tracking data.
    The data structure now uses a consistent English naming convention.
    """
    time_tracking_data = [
        {'name': 'Wolfgang Klein', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Julia Wagner', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Holger Frank', 'contract_hours': 8.0, 'start_time': '09:00', 'end_time': '17:00'},
        {'name': 'Lukas Müller', 'contract_hours': 8.0, 'start_time': '07:30', 'end_time': '17:30'},
        {'name': 'Jörg Bauer', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '15:30'},
        {'name': 'Werner Vogel', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Michael Becker', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Monika Wolf', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Sabine Schulz', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Claudia Adler', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Klaus Schäfer', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Bernd Neumann', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Peter Schmidt', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '18:00'},
        {'name': 'Heike Schwarz', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Andreas Hoffmann', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Dieter Zimmermann', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Petra Richter', 'contract_hours': 8.0, 'start_time': '09:00', 'end_time': '16:00'},
        {'name': 'Susanne Koch', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Ursula Krüger', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Hanna Schmitt', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Thomas Fischer', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Kristina Meier', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
        {'name': 'Lennart Weber', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '17:00'},
        {'name': 'Karl Braun', 'contract_hours': 8.0, 'start_time': '08:00', 'end_time': '16:00'},
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
   
    # --- CONFIGURATION ---
    # We still need the rule for the maximum work time.
    MAX_ARBEITSZEIT = 10.0

    # --- DATA SOURCE ---
    # We load the data from our new function.
    all_data = load_time_tracking_data()

    # --- Step 2: Prepare result variables (from your v1.2) ---
    zehn_stunden_mitarbeiter = []
    ueberstunden_mitarbeiter = []
    minusstunden_mitarbeiter = []
    
    # We don't need the counters anymore, we can get the number from the list length.

    # --- Step 3: Analyze the data (adapted logic) ---
    # We loop through the list of employees one by one.
    for employee_record in all_data:
        # Get the data for the current employee.
        name = employee_record['name']
        contract_hours = employee_record['contract_hours']
        start_time = employee_record['start_time']
        end_time = employee_record['end_time']

        # THIS IS THE KEY CHANGE:
        # Instead of reading the hours, we now calculate them.
        worked_hours = calculate_hours(start_time, end_time)

        # The rest is your original logic, adapted to the new variables.
        if worked_hours >= MAX_ARBEITSZEIT:
            zehn_stunden_mitarbeiter.append(name)
        elif worked_hours > contract_hours:
            ueberstunden_mitarbeiter.append(name)
        elif worked_hours < contract_hours:
            minusstunden_mitarbeiter.append(name)

    # --- Step 4: Print the results (exactly like in your v1.2) ---
    print("--- Analyse der Arbeitszeiten ---")

    print(f"\nWARNUNG! {len(zehn_stunden_mitarbeiter)} haben gegen das ArbZG verstoßen.")
    print(f"Namen: {zehn_stunden_mitarbeiter}")

    print(f"\nINFO: {len(ueberstunden_mitarbeiter)} Mitarbeiter haben Überstunden geleistet.")
    print(f"Namen: {ueberstunden_mitarbeiter}")

    print(f"\nHINWEIS: {len(minusstunden_mitarbeiter)} Mitarbeiter haben Minusstunden gemacht.")
    print(f"Namen: {minusstunden_mitarbeiter}")

    print("\n--- Analyse abgeschlossen ---")

# This is the standard way to start a Python program.
# The code inside this if-block only runs when the script is executed directly.
if __name__ == "__main__":
    main()
