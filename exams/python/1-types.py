# Grundlegende Datentypen

is_boolean: bool = True         # Wahrheitswert
num_integer: int = 2            # Ganzzahl
num_float: float = 3.1          # Gleitkommazahl
txt_string: str = "x"           # Zeichenkette

# Datentyp testen

print(type(is_boolean))         # >>> 'bool'

# Datentyp explizit verändern

to_int = int(num_float)         # 3.1 wird zu 3
to_float = float(num_integer)   # 2 wird zu 2.0
to_str = str(num_float)         # 3.1 wird zu "3.1"

# String-Konkatenierung

txt_concat = txt_string + "y"   # wird zu xy

# Sequenzielle Datenstrukturen

is_list = [0, 0, 0]             # veränderbare Liste
is_tupel = (0, 0, 0)            # unveränderbare Liste (Tupel)
is_dictionary = {               # assoziative Liste
    "gelb": 19,                 # strings als keys
    "grün": 20  
}