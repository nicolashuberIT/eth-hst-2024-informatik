# Grundlegende Datentypen

IS_BOOLEAN: bool = True         # Wahrheitswert
NUM_INTEGER: int = 2            # Ganzzahl
NUM_FLOAT: float = 3.1          # Gleitkommazahl
TXT_STRING: str = "x"           # Zeichenkette

# Datentyp testen

print(type(IS_BOOLEAN))         # >>> 'bool'

# Datentyp explizit verändern

TO_INT = int(NUM_FLOAT)         # 3.1 wird zu 3
TO_FLOAT = float(NUM_INTEGER)   # 2 wird zu 2.0
TO_STR = str(NUM_FLOAT)         # 3.1 wird zu "3.1"

# String-Konkatenierung

TXT_CONCAT = TXT_STRING + "y"   # wird zu xy