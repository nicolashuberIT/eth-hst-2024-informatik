# Musterlösung mit GitHub Copilot erstellt

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Zustände
EMPTY = "🪨"
YOUNG_TREE = "🌱"
GROWING_TREE = "🌿"
TREE = "🌳"
FIRE = "🔥"
FIREBREAK = "🚧"

# Simulationsparameter
size = 1000  # Grösse des Grids
grow_start = 0.5  # Wahrscheinlichkeit, dass zu Beginn ein Baum steht
p = 0.1  # Wahrscheinlichkeit, dass ein Baum wächst
lightning = 0.005  # Wahrscheinlichkeit, dass ein Blitz einschlägt
tEnd = 10000  # Anzahl der Zeiteinheiten


def setup() -> np.ndarray:
    """Erstellt die Ausgangssituation."""
    firebreak_prob = 0.05
    tree_prob = grow_start
    empty_prob = 1 - tree_prob - firebreak_prob
    grid = np.random.choice(
        [EMPTY, TREE, FIREBREAK],
        size=(size, size),
        p=[empty_prob, tree_prob, firebreak_prob],
    )
    return grid


def print_grid(grid: np.ndarray) -> None:
    """Gibt die Matrix in der Konsole aus."""
    os.system("clear")
    for row in grid:
        print(" ".join(row))
    print()


def burn(grid: np.ndarray, x: int, y: int) -> bool:
    """Bestimmt, ob eine Nachbarzelle brennt."""
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < size and 0 <= y + dy < size:
                if grid[x + dx, y + dy] == FIRE:
                    return True
    return False


def update(grid: np.ndarray) -> np.ndarray:
    """Berechnet die Zustände für eine nächste Zeiteinheit."""
    new_grid = grid.copy()
    for x in range(size):
        for y in range(size):
            if grid[x, y] == EMPTY and np.random.random() < p:
                new_grid[x, y] = YOUNG_TREE
            elif grid[x, y] == YOUNG_TREE:
                new_grid[x, y] = GROWING_TREE
            elif grid[x, y] == GROWING_TREE:
                new_grid[x, y] = TREE
            elif grid[x, y] == TREE:
                if burn(grid, x, y) or np.random.random() < lightning:
                    new_grid[x, y] = FIRE
            elif grid[x, y] == FIRE:
                new_grid[x, y] = EMPTY
    return new_grid


def count(grid: np.ndarray) -> int:
    """Zählt die brennenden Kompartimente."""
    return np.sum(grid == FIRE)


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

# Live-Animation
fig, ax = plt.subplots()


def update_animation(frame):
    global Grid
    Grid = update(Grid)
    ax.clear()
    ax.imshow(Grid == TREE, cmap="Greens", interpolation="nearest")
    ax.imshow(Grid == FIRE, cmap="Reds", interpolation="nearest", alpha=0.6)
    ax.imshow(Grid == FIREBREAK, cmap="Blues", interpolation="nearest", alpha=0.3)
    ax.set_title(f"Zeit: {frame}")


ani = FuncAnimation(fig, update_animation, frames=tEnd, repeat=False)
plt.show()
