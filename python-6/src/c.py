import numpy as np
import matplotlib.pyplot as plt

def print_grid():
 pass

def setup():
 pass

def burn():
 pass

def count():
 pass

def update():
 pass

# Zustände
EMPTY = "."
TREE  = "🌳"
FIRE  = "🔥"

#Simulationsparameter
size = 10           # Grösse des Grids
grow_start = 0.5    # Wahrscheinnlichkeit, dass zu Beginn ein Baum steht
p = 0.1             # Wahrscheinlichkeit, dass ein Baum wächst
lightning = 0.005   # Wahrscheinlichkeit, dass ein Blitz einschlägt

#Ausgangsmatrix
Grid = setup()
#Ausgabe Simulationsstart
print("Time: 0")
print_grid()