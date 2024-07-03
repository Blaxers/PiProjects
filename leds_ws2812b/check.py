#!/usr/bin/env python3
# Importuj wszystkie niezbędne pakiety do pracy z diodami LED na Raspberry Pi
import board
import neopixel

def is_neopixel_pin_in_use(pin):
    try:
        # Attempt to use the pin for another purpose
        led = LED(pin)
        return False  # If no exception, pin is not in use
    except:
        return True  # If exception, pin is in use

# Specify the GPIO pin you want to check
pin_to_check = 18  # Example GPIO pin

if is_neopixel_pin_in_use(pin_to_check):
    print(f"GPIO pin {pin_to_check} is in use by NeoPixel.")
else:
    print(f"GPIO pin {pin_to_check} is not in use by NeoPixel.")