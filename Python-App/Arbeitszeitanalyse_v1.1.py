#!/usr/bin/env python3
# This "Shebang" allows the script to be executed directly on Linux systems
# after setting the correct permissions (chmod +x).

# --- CONFIGURATION (v1.1) ---
# We define our business rules here as variables.
# This makes the code easier to read and maintain.
MAX_ARBEITSZEIT = 10
REGELARBEITSZEIT = 8

# --- DATA SOURCE (Version 1.0) ---
# In a real application, this data would come from a database.
zeiterfassung = [
    {'name': 'Wolfgang Klein', 'stunden': 8},
    {'name': 'Julia Wagner', 'stunden': 9},
    {'name': 'Holger Frank', 'stunden': 8},
    {'name': 'Lukas Müller', 'stunden': 10},
    {'name': 'Jörg Bauer', 'stunden': 7},
    {'name': 'Werner Vogel', 'stunden': 8},
    {'name': 'Michael Becker', 'stunden': 9},
    {'name': 'Monika Wolf', 'stunden': 8},
    {'name': 'Sabine Schulz', 'stunden': 9},
    {'name': 'Claudia Adler', 'stunden': 8},
    {'name': 'Klaus Schäfer', 'stunden': 9},
    {'name': 'Bernd Neumann', 'stunden': 8},
    {'name': 'Peter Schmidt', 'stunden': 10},
    {'name': 'Heike Schwarz', 'stunden': 8},
    {'name': 'Andreas Hoffmann', 'stunden': 9},
    {'name': 'Dieter Zimmermann', 'stunden': 8},
    {'name': 'Petra Richter', 'stunden': 7},
    {'name': 'Susanne Koch', 'stunden': 9},
    {'name': 'Ursula Krüger', 'stunden': 8},
    {'name': 'Hanna Schmitt', 'stunden': 8},
    {'name': 'Thomas Fischer', 'stunden': 9},
    {'name': 'Kristina Meier', 'stunden': 8},
    {'name': 'Lennart Weber', 'stunden': 9},
    {'name': 'Karl Braun', 'stunden': 8},
]

# --- Step 2: Prepare result variables ---
# Lists to collect the names of the employees.
zehn_stunden_mitarbeiter = []
ueberstunden_mitarbeiter = []
minusstunden_mitarbeiter = []

# Counters to store the number of employees in each category.
anzahl_zehn_stunden = 0
anzahl_ueberstunden = 0
anzahl_minusstunden = 0

# --- Step 3: Analyze the data ---
# Loop through the list of employees one by one.
for mitarbeiter in zeiterfassung:
    # Get the hours and the name from the current employee's dictionary.
    stunden = mitarbeiter['stunden']
    name = mitarbeiter['name']

     # We now use our configuration variables instead of "magic numbers"
    if stunden >= MAX_ARBEITSZEIT:
        zehn_stunden_mitarbeiter.append(name)
        anzahl_zehn_stunden += 1
    elif stunden > REGELARBEITSZEIT:
        ueberstunden_mitarbeiter.append(name)
        anzahl_ueberstunden += 1
    elif stunden < REGELARBEITSZEIT:
        minusstunden_mitarbeiter.append(name)
        anzahl_minusstunden += 1

# --- Step 4: Print the results ---
print("--- Analyse der Arbeitszeiten ---")

# Output for employees with 10 or morehours.
print(f"\nWARNUNG! {anzahl_zehn_stunden} haben gegen das ArbZG verstoßen.")
print(f"Namen: {zehn_stunden_mitarbeiter}")

# Output for employees with 9 hours.
print(f"\nINFO: {anzahl_ueberstunden} Mitarbeiter haben Überstunden geleistet.")
print(f"Namen: {ueberstunden_mitarbeiter}")

# Output for employees with less than 8 hours.
print(f"\nHINWEIS: {anzahl_minusstunden} Mitarbeiter haben Minusstunden gemacht.")
print(f"Namen: {minusstunden_mitarbeiter}")

print("\n--- Analyse abgeschlossen ---")

