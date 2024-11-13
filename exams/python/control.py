IS_BOOLEAN: bool = True
NUM_INTEGER: int = 2
NUM_FLOAT: float = 3.1
TXT_STRING: str = "x"

# Verzweigungen

if IS_BOOLEAN:                  # if True
    pass
elif NUM_INTEGER < 0:           # if 2 < 0
    pass
else:                           # any other scenario
    pass

# for-Schleifen

for i in range(0, 3):          # >>> x0, x1, x2, 
    print(f"{TXT_STRING}{i}", end=", ")

for i in range(0, 4, 2):       # >>> x0, x2
    print(f"{TXT_STRING}{i}", end=", ")

# while-Schleifen

print()

i = 0
while i < 3:                   # >>> x0, x1, x2
    print(f"{TXT_STRING}{i}", end=", ")
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
    NUM_FLOAT / 0
except ZeroDivisionError as e:  # >>> Fehler! Division durch 0 nicht erlaubt: float division by zero
    print(f"Fehler! Division durch 0 nicht erlaubt: {e}")