# imports

import os
import time
import random
import matplotlib.pyplot as plt

# settings

tend = 100
delay = 1
p = 0.3
size = 52

# functions

def setup(size):
  A = [[0 for x in range(size)] for y in range(size)]
  return A

def output(grid, zeiteinheit):
  print("Tag ", zeiteinheit)
  for i in range(1, len(grid)-1):
    for j in range(1, len(grid)-1):
      if grid[i][j] > 0 and grid[i][j] < 8:
        if j == len(grid)-2:
          print(grid[i][j])
        else:
          print(grid[i][j], end=" ")
      else:
        if j == len(grid)-2:
          print(" ")
        else:
          print(" ", end=" ")
  print()
 
def count(grid):
  result = [0,0,0]
  for i in range(1, len(grid)-1):
    for j in range(1, len(grid)-1):
      if grid[i][j] == 0:
        result[0] += 1
      elif grid[i][j] > 0 and grid[i][j] < 8:
        result[1] += 1
      else:
        result[2] += 1
  return result

def update(B, p):
  C = B
  for i in range(1, len(B)-1):
    for j in range(1, len(B)-1):
      rand = random.random()
      if B[i][j] == 0:
        if B[i+1][j] > 0  and B[i+1][j] < 8 or B[i][j-1] > 0 and B[i][j-1] < 8 or B[i][j+1] > 0 and B[i][j+1] < 8 or B[i-1][j] > 0 and B[i-1][j] < 8:
          if rand <= p:
            C[i][j] = 1
          else:
            C[i][j] = 0
      elif B[i][j] > 0 and B[i][j] < 8:
        C[i][j] += 1
  return C

def visual(infiziert):
  plt.plot(infiziert)
  plt.ylabel('Anzahl Infizierte')
  plt.xlabel('Zeit')
  plt.savefig("/Users/nicolas/Desktop/Git/Lara/eth-hst-2024-informatik/python-4/src/assets/visual.png")

# main program

grid = setup(size)
grid[random.randint(1, len(grid)-1)][random.randint(1, len(grid)-1)] = 1

n_gesund = [0 for x in range(tend)]
n_infiziert =[0 for x in range(tend)]
n_genesen = [0 for x in range(tend)] 

output(grid, 0)

for i in range(0, tend):
  time.sleep(delay)
  os.system('clear')
  grid = update(grid, p)
  output(grid, i+1)
  result = count(grid)
  n_gesund[i] = result[0]
  n_infiziert[i] = result[1]
  n_genesen[i] = result[2]
  print("Gesund: \t", result[0],"\t(", round(result[0]/(len(grid)-2)**2 *100,2),"%)" )
  print("Infiziert: \t", result[1],"\t(", round(result[1]/(len(grid)-2)**2 *100,2),"%)")
  print("Genesen: \t", result[2],"\t(", round(result[2]/(len(grid)-2)**2 *100,2),"%)")

visual(n_infiziert)