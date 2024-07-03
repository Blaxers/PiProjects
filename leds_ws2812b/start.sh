#!/bin/bash

# Definiowanie czasów w formacie HH:MM
time_on="18:00"
time_off="22:00"

# Funkcja konwertująca czas HH:MM na sekundy od północy
time_to_seconds() {
  IFS=: read -r h m <<< "$1"
  echo $((10#$h * 3600 + 10#$m * 60))
}

# Funkcja obliczająca ile sekund pozostało do danego czasu (HH:MM)
seconds_until() {
  local target_time=$1
  local current_time=$(date "+%H:%M")
  local target_seconds=$(time_to_seconds "$target_time")
  local current_seconds=$(time_to_seconds "$current_time")
  if (( current_seconds <= target_seconds )); then
    echo $((target_seconds - current_seconds))
  else
    echo $((24*3600 - current_seconds + target_seconds))
  fi
}

while true; do
  now=$(date "+%H:%M")
  now_sec=$(time_to_seconds "$now")
  time_on_sec=$(time_to_seconds "$time_on")
  time_off_sec=$(time_to_seconds "$time_off")

  if (( now_sec >= time_on_sec && now_sec < time_off_sec )); then
    # Uruchomienie skryptu turn_on.py
    python3 turn_on.py

    # Obliczenie ile czasu zostało do 22:00 i odczekanie tego czasu
    seconds_left=$(seconds_until "$time_off")
    echo "Światło włączone. Pozostało $seconds_left sekund do 22:00."
    sleep "$seconds_left"

    # Po 22:00 uruchomienie skryptu turn_off.py
    python3 turn_off.py

  else
    # Jeśli jest po 22:00, uruchomienie skryptu turn_off.py, jeśli jeszcze nie zostało uruchomione
    if (( now_sec >= time_off_sec )); then
      python3 turn_off.py
    fi

    # Obliczenie ile czasu zostało do 18:00 następnego dnia i odczekanie tego czasu
    seconds_left=$(seconds_until "$time_on")
    echo "Światło wyłączone. Pozostało $seconds_left sekund do 18:00."
    sleep "$seconds_left"

    # Po 18:00 uruchomienie skryptu turn_on.py
    python3 turn_on.py
  fi
done
