IS_BOOLEAN: bool = True
NUM_INTEGER: int = 2
NUM_FLOAT: float = 3.1

# Arithmetische Operatoren

addition = NUM_INTEGER + NUM_FLOAT            # 2 + 3.1 = 5.1
subtraktion = NUM_INTEGER - NUM_FLOAT         # 2 - 3.1 = -1.1
multiplikation = NUM_INTEGER * NUM_FLOAT      # 2 * 3.1 = 6.2
division_normal = NUM_INTEGER / NUM_FLOAT     # 2 / 3.1 = 0.6451612903
division_special = NUM_FLOAT // NUM_INTEGER   # 3.1 // 2 = 1 (Division ohne Nachkommastellen)
modulo = NUM_FLOAT % NUM_INTEGER              # 3.1 % 2 = 1.1 (Rest einer Division)
potenz = NUM_INTEGER ** NUM_FLOAT             # 2 ** 3.1 = 8.5741877003

# Relatione Operatoren (vergleichen alle Datentypen ausser bool)

print(NUM_INTEGER > NUM_FLOAT)                # >>> False
print(NUM_INTEGER < NUM_FLOAT)                # >>> True
print(NUM_INTEGER == NUM_FLOAT)               # >>> False
print(NUM_INTEGER != NUM_FLOAT)               # >>> True
print(NUM_INTEGER >= NUM_FLOAT)               # >>> False
print(NUM_INTEGER <= NUM_FLOAT)               # >>> True

# Logische Operatoren (vergleichen bool)

print(not True)                               # >>> False
print(True and False)                         # >>> False
print(True or False)                          # >>> True

# Ausdrücke

NUM_INTEGER += 1                              # 2 + 1 = 3
NUM_INTEGER -+ 1                              # 2 - 1 = 1