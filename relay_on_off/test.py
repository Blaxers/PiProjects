#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
# Set the GPIO pin number
PIN_RELAY = 23  # GPIO16

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Setup the GPIO pin as output
GPIO.setup(PIN_RELAY, GPIO.OUT)

try:
    print("Turning on relay")
    GPIO.output(PIN_RELAY, GPIO.HIGH)
    time.sleep(1)

except KeyboardInterrupt:
    pass  # This will end the script with CTRL+C

finally:
    # Turn off the relay before cleanup
    GPIO.output(PIN_RELAY, GPIO.LOW)
    # Cleanup GPIO
    GPIO.cleanup()
