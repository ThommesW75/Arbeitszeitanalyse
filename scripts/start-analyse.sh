#!/bin/bash
# Dieses Skript startet eine neue, interaktive Sitzung
# mit der Arbeitszeitanalyse-Anwendung im laufenden Container.

echo "Starte interaktive Sitzung mit dem Arbeitszeitanalyse-Service..."
echo "---------------------------------------------------------"

# Dieser Befehl startet das Python-Skript in einer frischen, interaktiven
# Sitzung (-it) innerhalb des bereits laufenden Containers (arbeitszeitanalyse).
docker exec -it arbeitszeitanalyse python3 ./Arbeitszeitanalyse.py
