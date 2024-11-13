TXT_STRING: str = "test"
NUM_FLOAT: float = 3.1

# Einfache Ausgaben

print("test")                   # >>> test
print(TXT_STRING)               # >>> test
print(NUM_FLOAT)                # >>> 3.1

# Konkatenierte Ausgaben

print("str: ", TXT_STRING)      # >>> str: test
print(f"float: {NUM_FLOAT}")    # >>> float: 3.1 (sog. f-string)

# Sonderfälle

print("Meine\tAusgabe")         # >>> Meine     Ausgabe (Tab)

print("Meine\nAusgabe")         # >>> Meine
                                # >>> Ausgabe (Zeilenumbruch)

print("Meine", end="")          # unterdrückt Zeilenumbruch mit end="" 
print("Ausgabe")                # >>> MeineAusgabe

# Eingaben

INPUT = int(input("Test:" ))    # erfdert Eingabe in Konsole und forciert INPUT: int

# Konsole leeren

import os                       # Modul os (Operating System)
os.system('clear')              # löscht Konsoleninhalt