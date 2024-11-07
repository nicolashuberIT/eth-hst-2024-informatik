# Imports

import random

# Variablen

m = 3 # Anzahl Spielende
n = 5 # Anzahl Runden

rand = True # Zufallszahlen einschalten

# Listen bereitstellen

resultate = [[0 for x in range(n)] for y in range(m)]
summen = [0 for x in range(m)] # liegt hier ein Fehler im Skript vor? man muss m verwenden, um die Ausgabe in der Aufgabenstellung zu erzielen.

# Listen ausgeben

print(f"Punkte der {m} Spielenden über {n} Runden:")
print(resultate)
print()
print("Totalpunkte:")
print(summen)
print()

# Resultate einlesen

for i in range(n):
    print(f"Runde {i + 1}:")

    for j in range(m):
        print(f"Spieler {j + 1}")

        if rand:
            wert = random.randint(0, 10)
        else:
            wert = input("Wert: ")
        resultate[j][i] = int(wert)


        j += 1

    i += 1

# Summen berechnen

for k, resultat in enumerate(resultate):
    print(resultat)
    summen[k] = sum(resultat)

# Resultat ausgeben

print()
print(f"Punkte der {m} Spielenden über {n} Runden:")
print(resultate)
print()
print("Totalpunkte:")
print(summen)