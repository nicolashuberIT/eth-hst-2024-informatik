is_boolean: bool = True
num_integer: int = 2
num_float: float = 3.1
txt_string: str = "x"

# Verzweigungen

if is_boolean:                  # if True
    pass
elif num_integer < 0:           # if 2 < 0
    pass
else:                           # any other scenario
    pass

# for-Schleifen

for i in range(0, 3):          # >>> x0, x1, x2, 
    print(f"{txt_string}{i}", end=", ")

for i in range(0, 4, 2):       # >>> x0, x2
    print(f"{txt_string}{i}", end=", ")

# while-Schleifen

i = 0
while i < 3:                   # >>> x0, x1, x2
    print(f"{txt_string}{i}", end=", ")
    i += 1

# Schleifenablauf beeinflussen

for j in range(0, 10):          # >>> 0, 1, 3, 4, 
    if j == 1:                  # pass if j == 1
        pass

    if j == 2:                  # continue to next iteration if j == 2
        continue

    if j == 5:                  # break loop if j == 5
        break

    print(j, end=", ")

# Ausnahmebehandlung

try:
    num_float / 0
except ZeroDivisionError as e:  # >>> Fehler! Division durch 0 nicht erlaubt: float division by zero
    print(f"Fehler! Division durch 0 nicht erlaubt: {e}")