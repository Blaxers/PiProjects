#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers
PIN_RELAY_1 = 22  # GPIO16
PIN_RELAY_2 = 23  # GPIO20

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Setup the GPIO pins as outputs
GPIO.setup(PIN_RELAY_1, GPIO.OUT)
GPIO.setup(PIN_RELAY_2, GPIO.OUT)

# Variables to store previous pin states
previous_pin_states = {'PIN1': None, 'PIN2': None}

# Function to read pin state from file
def read_pin_state(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            pin_states = {}
            for line in lines:
                parts = line.strip().split('=')
                if len(parts) == 2:
                    pin_states[parts[0].strip()] = parts[1].strip().lower() == 'true'
            return pin_states
    except FileNotFoundError:
        return {}

# Main loop to control relays
try:
    while True:
        pin_states = read_pin_state('pin_state')

        # Check for changes in PIN1 state
        if 'PIN1' in pin_states and pin_states['PIN1'] != previous_pin_states['PIN1']:
            if pin_states['PIN1']:
                GPIO.output(PIN_RELAY_1, GPIO.HIGH)
                print("Relay 1 is turned ON")
            else:
                GPIO.output(PIN_RELAY_1, GPIO.LOW)
                print("Relay 1 is turned OFF")
            previous_pin_states['PIN1'] = pin_states['PIN1']

        # Check for changes in PIN2 state
        if 'PIN2' in pin_states and pin_states['PIN2'] != previous_pin_states['PIN2']:
            if pin_states['PIN2']:
                GPIO.output(PIN_RELAY_2, GPIO.HIGH)
                print("Relay 2 is turned ON")
            else:
                GPIO.output(PIN_RELAY_2, GPIO.LOW)
                print("Relay 2 is turned OFF")
            previous_pin_states['PIN2'] = pin_states['PIN2']

        time.sleep(1)

except KeyboardInterrupt:
    pass  # This will end the script with CTRL+C

finally:
    # Cleanup GPIO
    GPIO.cleanup()
