#!/usr/bin/env python3
# Importuj wszystkie niezbędne pakiety do pracy z diodami LED na Raspberry Pi
import board
import neopixel
# Zainicjuj zmienną strips, podając pin danych GPIO
# wykorzystywany i ilość węzłów LED na taśmie oraz jasność (wartość od 0 do 1)
pixels1 = neopixel.NeoPixel(board.D18, 144, brightness=0.2)

# Ustaw wszystkie diody na stały kolor czerwony
pixels1.fill((255, 0, 0))