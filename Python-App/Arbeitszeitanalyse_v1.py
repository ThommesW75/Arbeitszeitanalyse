#!/usr/bin/env python3
# This "Shebang" allows the script to be executed directly on Linux systems
# after setting the correct permissions (chmod +x).

# --- DATA SOURCE (Version 1.0) ---
# In a real application, this data would come from a database.
# For our first version, we define it directly in the code.
zeiterfassung = [
    {'name': 'Wolfgang Klein', 'stunden': 8},
    {'name': 'Julia Wagner', 'stunden': 9},
    {'name': 'Holger Frank', 'stunden': 8},
    {'name': 'Lukas Müller', 'stunden': 10},
    {'name': 'Jörg Bauer', 'stunden': 7.5},
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
neun_stunden_mitarbeiter = []
unterstunden_mitarbeiter = []

# Counters to store the number of employees in each category.
anzahl_zehn_stunden = 0
anzahl_neun_stunden = 0
anzahl_unterstunden = 0

# --- Step 3: Analyze the data ---
# Loop through the list of employees one by one.
for mitarbeiter in zeiterfassung:
    # Get the hours and the name from the current employee's dictionary.
    stunden = mitarbeiter['stunden']
    name = mitarbeiter['name']

    # Analyzing the working hours.
    if stunden == 10:
        zehn_stunden_mitarbeiter.append(name)
        anzahl_zehn_stunden += 1
    elif stunden == 9:
        neun_stunden_mitarbeiter.append(name)
        anzahl_neun_stunden += 1
    elif stunden < 8: 
        unterstunden_mitarbeiter.append(name)
        anzahl_unterstunden += 1

# --- Step 4: Print the results ---
print("--- Analyse der Arbeitszeiten ---")

# Output for employees with 10 or morehours.
print(f"\nWARNUNG! {anzahl_zehn_stunden} haben gegen das ArbZG verstoßen.")
print(f"Namen: {zehn_stunden_mitarbeiter}")

# Output for employees with 9 hours.
print(f"\nINFO: {anzahl_neun_stunden} Mitarbeiter haben Überstunden geleistet.")
print(f"Namen: {neun_stunden_mitarbeiter}")

# Output for employees with less than 8 hours.
print(f"\nHINWEIS: {anzahl_unterstunden} Mitarbeiter haben Minusstunden gemacht.")
print(f"Namen: {unterstunden_mitarbeiter}")

print("\n--- Analyse abgeschlossen ---")

