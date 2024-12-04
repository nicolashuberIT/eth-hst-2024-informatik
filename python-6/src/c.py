# Musterlösung mit GitHub Copilot erstellt und manuell angepasst

import os
import time
import numpy as np
import matplotlib.pyplot as plt

# Zustände
EMPTY = "🪨"
TREE = "🌳"
FIRE = "🔥"

# Simulationsparameter
size = 50  # Grösse des Grids
grow_start = 0.5  # Wahrscheinlichkeit, dass zu Beginn ein Baum steht
p = 0.1  # Wahrscheinlichkeit, dass ein Baum wächst
lightning = 0.005  # Wahrscheinlichkeit, dass ein Blitz einschlägt
tEnd = 100  # Anzahl der Zeiteinheiten


def setup() -> np.ndarray:
    grid = np.random.choice(
        [EMPTY, TREE], size=(size, size), p=[1 - grow_start, grow_start]
    )
    return grid


def print_grid(grid: np.ndarray) -> None:
    time.sleep(0.5)
    os.system("clear")
    for row in grid:
        print(" ".join(row))
    print()


def burn(grid: np.ndarray, x: int, y: int) -> bool:  # Prüft ob Baum in der Nähe brennt
    for dx in [
        -1,
        0,
        1,
    ]:  # Schleife über die Nachbarzellen in x-Richtung (Schleife wird für jeden Wert in der Liste ausgeführt)

        for dy in [-1, 0, 1]:  # Schleife über die Nachbarzellen in y-Richtung
            if dx == 0 and dy == 0:
                continue

            if 0 <= x + dx < size and 0 <= y + dy < size:
                if grid[x + dx, y + dy] == FIRE:
                    return True

    return False


def update(
    grid: np.ndarray,
) -> np.ndarray:  # Berechnet Zustände für nächste Zeiteinheit
    new_grid = grid.copy()

    for x in range(size):
        for y in range(size):

            if (
                grid[x, y] == EMPTY and np.random.random() < p
            ):  # np.random.random() gibt eine Zufallszahl zwischen 0 und 1 zurück
                new_grid[x, y] = TREE
            elif grid[x, y] == TREE:
                if burn(grid, x, y) or np.random.random() < lightning:
                    new_grid[x, y] = FIRE
            elif grid[x, y] == FIRE:
                new_grid[x, y] = EMPTY

    return new_grid


def count(grid: np.ndarray) -> int:  # Zählt die brennenden Kompartimente
    return np.sum(grid == FIRE)  # np.sum() berechnet die Summe der Elemente


# Ausgangsmatrix
Grid = setup()

# Liste zur Speicherung der Anzahl brennender Zellen
fire_counts = []

# Ausgabe Simulationsstart
print("Time: 0")
print_grid(Grid)

# Simulation über die Zeit t bis tEnd
for t in range(1, tEnd + 1):
    Grid = update(Grid)
    fire_counts.append(count(Grid))
    print(f"Time: {t}")
    print_grid(Grid)

# Grafische Darstellung der Resultate über die Zeit
plt.plot(range(1, tEnd + 1), fire_counts)
plt.xlabel("Zeit")
plt.ylabel("Anzahl brennender Zellen")
plt.title("Waldbrand-Simulation")
plt.show()
