txt_string: str = "test"
num_float: float = 3.1

# Einfache Ausgaben

print("test")                   # >>> test
print(txt_string)               # >>> test
print(num_float)                # >>> 3.1

# Konkatenierte Ausgaben

print("str: ", txt_string)      # >>> str: test
print(f"float: {num_float}")    # >>> float: 3.1 (sog. f-string)

# Sonderfälle

print("Meine\tAusgabe")         # >>> Meine     Ausgabe (Tab)

print("Meine\nAusgabe")         # >>> Meine
                                # >>> Ausgabe (Zeilenumbruch)

print("Meine", end="")          # unterdrückt Zeilenumbruch mit end="" 
print("Ausgabe")                # >>> MeineAusgabe

# Eingaben

input = int(input("Test:" ))    # erfdert Eingabe in Konsole und forciert INPUT: int

# Konsole leeren

import os                       # Modul os (Operating System)
os.system('clear')              # löscht Konsoleninhalt