#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# Relay 1
GPIO.setup(23, GPIO.OUT)
# Relay 2
GPIO.setup(24, GPIO.OUT)

try:
    while True:
        GPIO.output(23, GPIO.HIGH)
        print('Relay 1 ON')
        time.sleep(1)
        GPIO.output(24, GPIO.HIGH)
        print('Relay 2 ON')
        time.sleep(1)
        GPIO.output(23, GPIO.LOW)
        print('Relay 1 OFF')
        time.sleep(1)
        GPIO.output(24, GPIO.LOW)
        print('Relay 2 OFF')
        time.sleep(1)

finally:
    GPIO.cleanup()