#!/usr/bin/env python3
# Importuj wszystkie niezbędne pakiety do pracy z diodami LED na Raspberry Pi
import board
import neopixel
pixels1 = neopixel.NeoPixel(board.D18, 144, brightness=0.2)
# Ustaw wszystkie diody na stały kolor czerwony
pixels1.fill((0, 0, 0))


