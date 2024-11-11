# imports

import os
import time
import random
from typing import List
import matplotlib.pyplot as plt

# settings

GRID_SIZE: int = 48 
END_TIME: int = 100
ITERATION_DELAY: int = 1
INFECTION_PROBABILITY: float = 0.3
PLOT_OUTPUT: str = "/Users/nicolas/Desktop/Git/Lara/eth-hst-2024-informatik/python-4/src/assets/visual.png"

# functions

def main(grid_size: int, end_time: int, infection_prob: float, delay: float, plot_output: str) -> None:
    grid = setup(grid_size)
    
    # Seed an initial infection at a random location within the grid
    initial_x, initial_y = random.randint(1, len(grid)-2), random.randint(1, len(grid)-2)
    grid[initial_x][initial_y] = 1

    # Initialize lists to track the number of healthy, infected, and recovered cells over time
    n_healthy: List[int] = [0] * end_time
    n_infected: List[int] = [0] * end_time
    n_recovered: List[int] = [0] * end_time

    # Display initial state
    output(grid, 0)

    # Simulation loop
    for t in range(end_time):
        time.sleep(delay)
        os.system('clear')

        grid = update(grid, infection_prob)
        output(grid, t + 1)

        # Count cell types
        healthy, infected, recovered = count(grid)
        
        # Store counts for visualization
        n_healthy[t] = healthy
        n_infected[t] = infected
        n_recovered[t] = recovered

        # Print summary of the current state
        total_cells = (grid_size - 2) ** 2  # Exclude the borders
        print(f"Gesund: \t{healthy}\t({round(healthy / total_cells * 100, 2)}%)")
        print(f"Infiziert: \t{infected}\t({round(infected / total_cells * 100, 2)}%)")
        print(f"Genesen: \t{recovered}\t({round(recovered / total_cells * 100, 2)}%)")
    
    visual(n_infected, plot_output)

def setup(size: int) -> List[List[int]]:
    return [[0] * size for _ in range(size)]

def output(grid: List[List[int]], time_unit: int) -> None:
    print(f"Day {time_unit}")

    rows, cols = len(grid), len(grid[0])

    for i in range(1, rows - 1):
        row_output = []

        for j in range(1, cols - 1):
            if 0 < grid[i][j] < 8:
                row_output.append(str(grid[i][j]))
            else:
                row_output.append(" ")

        print(" ".join(row_output))

    print()
 
def count(grid: List[List[int]]) -> List[int]:
    result = [0, 0, 0]  # [count_zeros, count_between_1_and_7, count_8_or_more]
    
    rows, cols = len(grid), len(grid[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            cell_value = grid[i][j]
            
            if cell_value == 0:
                result[0] += 1
            elif 1 <= cell_value < 8:
                result[1] += 1
            else:
                result[2] += 1

    return result

def update(grid: List[List[int]], probability: float) -> List[List[int]]:
    updated_grid = grid
    rows, cols = len(grid), len(grid[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            current_cell = grid[i][j]
            rand_val = random.random()

            if current_cell == 0:
                neighbors = [
                    grid[i+1][j],  # below
                    grid[i][j-1],  # left
                    grid[i][j+1],  # right
                    grid[i-1][j]   # above
                ]

                if any(1 <= neighbor < 8 for neighbor in neighbors):
                    updated_grid[i][j] = 1 if rand_val <= probability else 0

            elif 1 <= current_cell < 8:
                updated_grid[i][j] += 1

    return updated_grid

def visual(infiziert, output_path):
  plt.plot(infiziert)
  plt.ylabel('Anzahl Infizierte')
  plt.xlabel('Zeit')
  plt.savefig(output_path)

if __name__ == "__main__":
    main(GRID_SIZE, END_TIME, INFECTION_PROBABILITY, ITERATION_DELAY, PLOT_OUTPUT)