is_boolean: bool = True
num_integer: int = 2
num_float: float = 3.1

# Arithmetische Operatoren

addition = num_integer + num_float            # 2 + 3.1 = 5.1
subtraktion = num_integer - num_float         # 2 - 3.1 = -1.1
multiplikation = num_integer * num_float      # 2 * 3.1 = 6.2
division_normal = num_integer / num_float     # 2 / 3.1 = 0.6451612903
division_special = num_float // num_integer   # 3.1 // 2 = 1 (Division ohne Nachkommastellen)
modulo = num_float % num_integer              # 3.1 % 2 = 1.1 (Rest einer Division)
potenz = num_integer ** num_float             # 2 ** 3.1 = 8.5741877003

# Relatione Operatoren (vergleichen alle Datentypen ausser bool)

print(num_integer > num_float)                # >>> False
print(num_integer < num_float)                # >>> True
print(num_integer == num_float)               # >>> False
print(num_integer != num_float)               # >>> True
print(num_integer >= num_float)               # >>> False
print(num_integer <= num_float)               # >>> True

# Logische Operatoren (vergleichen bool)

print(not True)                               # >>> False
print(True and False)                         # >>> False
print(True or False)                          # >>> True

# Ausdrücke

num_integer += 1                              # 2 + 1 = 3
num_integer -+ 1                              # 2 - 1 = 1