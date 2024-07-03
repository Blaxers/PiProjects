#!/usr/bin/env python3
# Importuj wszystkie niezbędne pakiety do pracy z diodami LED na Raspberry Pi
import time
import board
import neopixel

try:
    # Zainicjuj zmienną strips, podając pin danych GPIO
    # wykorzystywany i ilość węzłów LED na taśmie oraz jasność (wartość od 0 do 1)
    pixels1 = neopixel.NeoPixel(board.D18, 144, brightness=0.2)

    # Ustaw wszystkie diody na stały kolor czerwony
    pixels1.fill((255, 0, 0))

    # Poczekaj przez 2 godziny (czas trwania)
    czas_trwania = 2 * 60 * 60  # 2 godziny w sekundach
    time.sleep(czas_trwania)

except KeyboardInterrupt:
    # Przechwyć wyjątek, gdy użytkownik przerwie działanie skryptu (Ctrl+C)
    print("Przerwano przez użytkownika")
except Exception as e:
    # Przechwyć wszelkie inne wyjątki
    print("Wystąpił błąd:", e)
finally:
    # Wyłącz wszystkie diody LED
    pixels1.fill((0, 0, 0))