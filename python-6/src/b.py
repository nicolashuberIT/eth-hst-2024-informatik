#Musterlösung mit GitHub Copilot erstellt und manuell angepasst

import numpy as np
import random as rd
from typing import Tuple

# Spielfeld erstellen
def setup() -> np.ndarray:
    return np.full((3, 3), '.')

# Spielfeld ausgeben
def ausgabe(spielfeld: np.ndarray) -> None:
    print("  1 2 3")
    for i in range(3):
        print(f"{i + 1} {' '.join(spielfeld[i])}")
    print()

# Benutzereingabe für Koordinaten
def eingabe(spieler: str) -> Tuple[int, int]:
    while True:
        try:
            zeile = int(input(f"Spieler {spieler}, Zeile (1-3): ")) - 1
            spalte = int(input(f"Spieler {spieler}, Spalte (1-3): ")) - 1

            print()

            if 0 <= zeile < 3 and 0 <= spalte < 3:
                return zeile, spalte
        except ValueError:
            pass
        print("Ungültige Eingabe. Bitte erneut versuchen.")

# Zeichen setzen
def setze_zeichen(spielfeld: np.ndarray, zeile: int, spalte: int, zeichen: str) -> bool:
    if spielfeld[zeile, spalte] == '.':
        spielfeld[zeile, spalte] = zeichen
        return True
    return False

# Überprüfen, ob jemand gewonnen hat
def hat_gewonnen(spielfeld: np.ndarray, zeichen: str) -> bool:
    for i in range(3):
        if np.all(spielfeld[i, :] == zeichen):  # Zeilen
            return True
        if np.all(spielfeld[:, i] == zeichen):  # Spalten
            return True
    if np.all(np.diag(spielfeld) == zeichen):  # Diagonale
        return True
    if np.all(np.diag(np.fliplr(spielfeld)) == zeichen):  # Gegendiagonale
        return True
    return False

# Computerzug
def computer_zug(spielfeld: np.ndarray) -> Tuple[int, int]:
    freie_felder = np.argwhere(spielfeld == '.')
    return tuple(rd.choice(freie_felder))

# Hauptspielschleife
def spiel() -> None:
    spielfeld = setup()
    aktueller_spieler = 'X'
    while True:
        ausgabe(spielfeld)
        if aktueller_spieler == 'X':
            zeile, spalte = eingabe(aktueller_spieler)
        else:
            zeile, spalte = computer_zug(spielfeld)
            print(f"Computer setzt auf Zeile {zeile + 1}, Spalte {spalte + 1}")
        
        if setze_zeichen(spielfeld, zeile, spalte, aktueller_spieler):
            if hat_gewonnen(spielfeld, aktueller_spieler):
                ausgabe(spielfeld)
                print(f"Game over. Spieler {aktueller_spieler} hat gewonnen!")
                break
            aktueller_spieler = 'O' if aktueller_spieler == 'X' else 'X'
        else:
            print("Feld bereits belegt. Bitte erneut versuchen.")

if __name__ == "__main__":
    spiel()