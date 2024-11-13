# Sequenzielle Datentypen, Such- und Sortieralgorithmen, Sequenzanalyse

## Inhaltsverzeichnis

- [Sequenzielle Datentypen, Such- und Sortieralgorithmen, Sequenzanalyse](#sequenzielle-datentypen-such--und-sortieralgorithmen-sequenzanalyse)
  - [Inhaltsverzeichnis](#inhaltsverzeichnis)
  - [Struktur](#struktur)
  - [Lösungen](#lösungen)
    - [Anmerkungen](#anmerkungen)
    - [Übung C1](#übung-c1)
    - [Übung C2](#übung-c2)
    - [Übung C3](#übung-c3)
    - [Übung C4](#übung-c4)
    - [Übung C4 Extension](#übung-c4-extension)

## Struktur

Die Struktur dieses Dossiers ist wie folgt:

```txt
⎡ Aufgaben
⎢ ⟶ /src
⎢ ⟶ README.md
⎢ ⟶ README.pdf
⎣
```

Unter `/src` findest du alle Lösungen zu den C-Aufgaben aus dem Übungs-Dossier mit dem oben genannten Titel inkl. Erweiterungen.

## Lösungen
### Anmerkungen

Ich habe versucht, die Aufgaben möglichst gemäss der Theorie zu lösen. Auf die Ausgaben in die Konsole solltest du sicher einen Kontrollblick werfen, da ich nicht genau weiss, wie diese in Code Expert validiert werden. Habe jeweils eine Form gewählt, die ähnlich zum Beispiel in der Aufgabenstellung ist.

Der Code ist an manchen Stellen nicht so sauber. 🫣 Hoffe, das ist in Ordnung und nicht so schlimm. 😇

Hoffe, es stimmt alles. Bei Fragen einfach fragen. ❤️

### Übung C1

Beachte Kommentare im Code.

### Übung C2

Beachte Kommentare im Code.

### Übung C3

Beachte Kommentare im Code.

### Übung C4

Diese Aufgabe habe ich so gelöst, wie es in der Aufgabenstellung beschrieben ist. Besser ist eine Implementierung gemäss C4 Extension.

Beachte Kommentare im Code.

### Übung C4 Extension

Hier siehst du, wie ich diese Aufgabe auf meine Art gelöst hätte. Ich habe probiert, den Code sauber und übersichtlich zu halten. Der Code ist in Klassen organisiert, das Hauptprogramm findet sich in `main.py`.

In `c4-extension.py` findest du eine Implementierung des Programms, die du 1:1 in Code Expert einfügen kannst. Professioneller ist die Umsetzung gemäss `main.py` unter `c4-extension/`. Klassen werden üblicherweise in separate Files ausgelagert und als Dependencies importiert. Du kennst dieses Konzept unter dem Begriff Object Oriented Programming. 🤓

Die Struktur im Ordner `c4-extension` ist wie folgt:

```txt
⎡ c4-extension
⎢ ⟶ /src
⎢ ⟶ ⟶ Logger.py
⎢ ⟶ ⟶ SequenceAnalysis.py
⎢ ⟶ main.py
⎣
```

Die Klassen unter `/src` werden im Hauptprogramm `main.py` als Dependencies importiert. Ausserdem bedarf es einiger weiterer Dependencies, die entweder in den Klassen oder im Hauptprogramm importiert werden. Die meisten davon sind Teil der Python Standard Library, einige muss man separat installieren. Falls du bei der Ausführung von `c4-extension.py` oder `main.py` auf Probleme stossen solltest, kannst du in der Command Line von Code Expert den folgenden Befehl ausführen:

```txt
pip install numpy pandas
```

Auf diese Weise werden die erforderlichen Dependencies installiert und das Programm sollte reibungslos funktionieren. Falls es auf Code Expert nicht funktioniert, hier der vollständige Output gemäss der aktuellen Implementierung und den DNA-Sequenzen aus der Aufgabenstellung:

```txt
--------------------

The following cartesian product of the DNA_MAP keys are be used in the sequential analysis.

('Mabuya agilis', 'Mabuya agilis')
('Mabuya agilis', 'Mabuya atlantica')
('Mabuya agilis', 'Mabuya capensis')
('Mabuya agilis', 'Mabuya vittata')
('Mabuya atlantica', 'Mabuya agilis')
('Mabuya atlantica', 'Mabuya atlantica')
('Mabuya atlantica', 'Mabuya capensis')
('Mabuya atlantica', 'Mabuya vittata')
('Mabuya capensis', 'Mabuya agilis')
('Mabuya capensis', 'Mabuya atlantica')
('Mabuya capensis', 'Mabuya capensis')
('Mabuya capensis', 'Mabuya vittata')
('Mabuya vittata', 'Mabuya agilis')
('Mabuya vittata', 'Mabuya atlantica')
('Mabuya vittata', 'Mabuya capensis')
('Mabuya vittata', 'Mabuya vittata')

--------------------

The nucleotide analysis for each individual DNA sequence returns the following results:

Mabuya agilis:
--> A: 141
--> T: 98
--> G: 83
--> C: 101
--> -: 16
--> total: 439
Mabuya atlantica:
--> A: 140
--> T: 89
--> G: 86
--> C: 108
--> -: 16
--> total: 439
Mabuya capensis:
--> A: 145
--> T: 95
--> G: 78
--> C: 105
--> -: 16
--> total: 439
Mabuya vittata:
--> A: 142
--> T: 98
--> G: 81
--> C: 106
--> -: 12
--> total: 439

--------------------

The system has performed a length check of all given DNA sequences, which resolved with the following result:

--> Checked Mabuya agilis: 439 against Mabuya agilis: 439
--> Checked Mabuya atlantica: 439 against Mabuya agilis: 439
--> Checked Mabuya capensis: 439 against Mabuya agilis: 439
--> Checked Mabuya vittata: 439 against Mabuya agilis: 439

All given DNA sequences are of the same length. Check ok.

--------------------

The system has performed a DNA sequence comparison for all possible combinations of given DNA sequences, which resolved with the following result:

Comparison between Mabuya agilis and Mabuya agilis:
--> Total comparisons: 423
--> Similarities: 423
--> Similarity percentage: 100.00%
Comparison between Mabuya agilis and Mabuya atlantica:
--> Total comparisons: 419
--> Similarities: 372
--> Similarity percentage: 89.00%
Comparison between Mabuya agilis and Mabuya capensis:
--> Total comparisons: 414
--> Similarities: 364
--> Similarity percentage: 88.00%
Comparison between Mabuya agilis and Mabuya vittata:
--> Total comparisons: 419
--> Similarities: 391
--> Similarity percentage: 93.00%
Comparison between Mabuya atlantica and Mabuya agilis:
--> Total comparisons: 419
--> Similarities: 372
--> Similarity percentage: 89.00%
Comparison between Mabuya atlantica and Mabuya atlantica:
--> Total comparisons: 423
--> Similarities: 423
--> Similarity percentage: 100.00%
Comparison between Mabuya atlantica and Mabuya capensis:
--> Total comparisons: 417
--> Similarities: 379
--> Similarity percentage: 91.00%
Comparison between Mabuya atlantica and Mabuya vittata:
--> Total comparisons: 418
--> Similarities: 383
--> Similarity percentage: 92.00%
Comparison between Mabuya capensis and Mabuya agilis:
--> Total comparisons: 414
--> Similarities: 364
--> Similarity percentage: 88.00%
Comparison between Mabuya capensis and Mabuya atlantica:
--> Total comparisons: 417
--> Similarities: 379
--> Similarity percentage: 91.00%
Comparison between Mabuya capensis and Mabuya capensis:
--> Total comparisons: 423
--> Similarities: 423
--> Similarity percentage: 100.00%
Comparison between Mabuya capensis and Mabuya vittata:
--> Total comparisons: 415
--> Similarities: 364
--> Similarity percentage: 88.00%
Comparison between Mabuya vittata and Mabuya agilis:
--> Total comparisons: 419
--> Similarities: 391
--> Similarity percentage: 93.00%
Comparison between Mabuya vittata and Mabuya atlantica:
--> Total comparisons: 418
--> Similarities: 383
--> Similarity percentage: 92.00%
Comparison between Mabuya vittata and Mabuya capensis:
--> Total comparisons: 415
--> Similarities: 364
--> Similarity percentage: 88.00%
Comparison between Mabuya vittata and Mabuya vittata:
--> Total comparisons: 427
--> Similarities: 427
--> Similarity percentage: 100.00%

--------------------

The comparison results can be visualised in the following matrix:

                  Mabuya agilis  Mabuya atlantica  Mabuya capensis  Mabuya vittata
Mabuya agilis              1.00              0.89             0.88            0.93
Mabuya atlantica           0.89              1.00             0.91            0.92
Mabuya capensis            0.88              0.91             1.00            0.88
Mabuya vittata             0.93              0.92             0.88            1.00

--------------------

The program was successfully completed.

--------------------
```

Zum Abschluss ein Screenshot der Vergleichsresultate, welche du für die vollständige Matrix brauchst:

![Image can be found at assets/image.png](/assets/image.png)

Happy Coding :-)

---

© 2024, [Creative-Commons-Lizenz](/LICENSE.md) / [Nicolas Huber](https://nicolas-huber.ch).