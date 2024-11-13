# ASCII-Zeichen

print(ord("X"))                 # >>> 88 (int, Ordnungszahl von "X" in ASCII)
print(chr(88))                  # >>> X (str, Zeichen in ASCII für OZ 88)

# Zufallszahlen

import random as rd             # random-Modul mit Alias rd
rand_int = rd.randint(0, 10)    # Zufallszahl zwischen und inkl. 0 und 10, int
rand_float = rd.random()        # Zufallszahl zwischen und inkl. 0 und 1, float
rand_float = rd.uniform(0, 10)  # Zufallszahl zwischen und inkl. 0 und 10, float