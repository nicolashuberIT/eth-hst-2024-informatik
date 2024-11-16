# ASCII-Zeichen

print(ord("X"))                 # >>> 88 (int, Ordnungszahl von "X" in ASCII)
print(chr(88))                  # >>> X (str, Zeichen in ASCII für OZ 88)

# Zufallszahlen

import random as rd             # random-Modul mit Alias rd
rand_int = rd.randint(0, 10)    # Zufallszahl zwischen und inkl. 0 und 10, int
rand_float = rd.random()        # Zufallszahl zwischen 0 (inkl.) und 1 (exkl.), float
rand_float = rd.uniform(0, 10)  # Zufallszahl zwischen 0 und 10 (inklusive Grenzen), float

# String als Liste

txt_string = "test"
print(txt_string[1])            # >>> e

# Tupel und Listen

is_tupel = (1, 2, 3)            # unveränderbares Tupel mit 3 Elementen
is_list = ["test", 25, 3]       # eindimensionale Liste mit diversen Datentypen

is_list.append("neu")           # ["test", 25, 3, "neu"]
is_list.pop(0)                  # [25, 3, "neu"]
is_list.insert(0, "erste")      # ["erste", 25, 3, "neu"]

a_list = [5 for x in range(3)]  # Listenabstraktion, [5, 5, 5]
print(len(a_list))              # >>> 3 (Länge mit len())

# Dictionaries (assoziative Arrays (Listen))

is_dictionary = {               # assoziatives Array, sog. Dictionary
    "gelb": 19,
    "grün": 20
}

print(is_dictionary.keys())     # >>> dict_keys(['gelb', 'grün']) (dict_keys-Objekt)
print(is_dictionary.values())   # >>> dict_values([19, 20]) (dict_values-Objekt)
print(is_dictionary.items())    # >>> dict_items([('gelb', 19), ('grün', 20)]) (dict_items-Objekt)

is_dictionary["rot"] = 30          # {"gelb": 19, "grün": 20, "rot": 30}
is_dictionary.update({"blau": 25}) # {"gelb": 19, "grün": 20, "rot": 30, "blau": 25}

is_dictionary.pop("grün")       # {"gelb": 19, "rot": 30, "blau": 25}
del is_dictionary["gelb"]       # {"rot": 30, "blau": 25}
is_dictionary.popitem()         # {"rot": 30} (entfernt das zuletzt hinzugefügte Paar)
is_dictionary.clear()           # {}

# Indexierung von sequentiellen Datenstrukturen

print(is_tupel[0])              # >>> 1 (Indexierung mit eckigen Klammern)
print(is_list[0])               # >>> erste (Indexierung mit eckigen Klammern)
print(is_list[-1])              # >>> neu (Indexierung von hinten, beginnend mit -1)

print(is_tupel[:])              # >>> (1, 2, 3) (Slicing mit : gesamte Sequenz)
print(is_tupel[1:])             # >>> (2, 3) (Slicing von Index 1 bis Ende)
print(is_tupel[1:-1])           # >>> (2,) (Slicing von Index 1 bis -1, exklusive -1)

print(is_dictionary["gelb"])    # >>> 19 (Indexierung mit Schlüssel)

# Iteration über sequentielle Datenstrukturen

for i in range(0, len(is_list)): # Zugriff auf Liste mit Index
    print(is_list[i], end=",")   # >>> erste,25,3,neu,

for element in is_list:          # Zugriff auf Liste ohne Index
    print(element, end=",")      # >>> erste,25,3,neu,

for i, element in enumerate(is_list, 0): # Zugriff auf Elemente inkl. Index
    print(f"{i} = {element}", end=",")   # >>> 0 = erste,1 = 25,2 = 3,3 = neu,