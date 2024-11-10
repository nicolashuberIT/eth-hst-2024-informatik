import time
import os
import random
import matplotlib.pyplot as plt


def setup():
  A = [[0 for x in range(42)] for y in range(42)]
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
  for i in range(1, len(B)-1):
    for j in range(1, len(B)-1):
      rand = random.random()
      if B[i][j] == 0:
        if B[i+1][j] > 0  and B[i+1][j] < 8 or B[i][j-1] > 0 and B[i][j-1] < 8 or B[i][j+1] > 0 and B[i][j+1] < 8 or B[i-1][j] > 0 and B[i-1][j] < 8:
          if rand <= p:
            B[i][j] = 1
          else:
            B[i][j] = 0
      elif B[i][j] > 0 and B[i][j] < 8:
        B[i][j] += 1
  return B

def visual(infiziert):
  plt.plot(infiziert)
  plt.ylabel('Anzahl Infizierte')
  plt.xlabel('Zeit')
  plt.savefig("/Users/nicolas/Desktop/Git/Lara/eth-hst-2024-informatik/python-4/src/assets/visual.png")

#Hauptprogramm
tend = 100
grid = setup()
delay = 1
p = 0.3
n_gesund = [0 for x in range(tend)]
n_infiziert =[0 for x in range(tend)]
n_genesen = [0 for x in range(tend)]

#grid[random.randint(1, len(grid)-1)][random.randint(1, len(grid)-1)] = 1
grid[5][5] = 1
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