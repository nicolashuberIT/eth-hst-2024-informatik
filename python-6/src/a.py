#Musterlösung mit GitHub Copilot erstellt und manuell angepasst

import numpy as np
import random as rd
import matplotlib.pyplot as plt

# Entscheidung einer Kugel an einem Nagel
def entscheide_richtung() -> int:
    return 0 if rd.random() < 0.5 else 1 # rd.random() gibt eine Zufallszahl zwischen 0 und 1 zurück

# Position der Kugel nach Durchlauf mit dynamischer Höhe
def kugel_durchlauf(hoehe: int) -> int:
    position: int = 0
    for _ in range(hoehe): # _ wird als Platzhalter für Variablen verwendet, die nicht verwendet werden
        position += entscheide_richtung()
    return position

# Kugel-Behälter einbauen
def initialisiere_behaelter(hoehe: int) -> np.ndarray:
    return np.zeros(hoehe + 1, dtype=int) # dtype=int: Datentyp der Elemente im Array

# Zähler für viele Kugeln einbauen
def simuliere_galton_board(hoehe: int, anzahl_kugeln: int) -> np.ndarray:
    behaelter: np.ndarray = initialisiere_behaelter(hoehe) # np.ndarray: n-dimensionales Array
    for _ in range(anzahl_kugeln):
        position: int = kugel_durchlauf(hoehe)
        behaelter[position] += 1
    return behaelter

# Schritt 7: Visualisierung des Resultats
def visualisiere_resultat(behaelter: np.ndarray) -> None:
    plt.bar(range(len(behaelter)), behaelter)
    plt.xlabel('Behälter')
    plt.ylabel('Anzahl Kugeln')
    plt.title('Galton-Board')
    plt.show() # Zeile ersetzen in Code Expert der ETH Zürich

# Hauptprogramm
def main() -> None:
    hoehe: int = int(input("Höhe? --> "))
    anzahl_kugeln: int = int(input("Anzahl Kugeln? --> "))
    behaelter: np.ndarray = simuliere_galton_board(hoehe, anzahl_kugeln)
    print("Kugeln in den Behältern:", behaelter)
    visualisiere_resultat(behaelter)

if __name__ == "__main__":
    main()
    