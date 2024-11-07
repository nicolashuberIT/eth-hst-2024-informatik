# %%

# DNA Sequenzen der 4 Mabuya-Arten

m_agilis_seq    = "TTGTCTTTTAAATAAAGACCTGTATGAATGGCTGAATGAGGATAAACCTGTCTCTTATAACTAATCAGTGAAACTGATCTCCCAGTACAAAAGCTGGAATATACACATAAGACGAGAAGACCCTGTGGAGCTTAAAAC-AAACCACTAAACAA-----GT--ATACCACTACCTTAGTGTAC-GTTTTCAGTTGGGGCGACTTCGGAATAAAATGAAACTTCCGAGCACAGAGGCAC-TTCCTCTAACTAAGGCCAACAAGCCAAAGACCC---ATAAACGACCCGGCC---TTGCCGATCAACGAACCAAGTTACCCCAGGGATAACAGCGCAATCTTCTTCGAGAGCCCTTATCAACAAGAAGGTTTACGACCTCGATGTTGGATCAGGACACCCAAATGGTGCAGCCGCTATTAAAGGTTCGTTTGTTCAACGATT"
m_atlantica_seq = "TTGTCTTCTAAATAAAGACCAGTATGAACGGCTAAATGAGGACAAACCTGTCTCTTTTAACTAATCAGTGAAACTGATCTCCCAGTACAAAAGCTGGGATACAAACATAAGACGAGAAGACCCCGTGGAGCTTAAAACAAAACCACCAATCCA--C------GCCCTGG-ACCCTGGTGGACTGTTTTGAGTTGGGGCGACTTCGGAATAAAAAGAAACTTCCGAGCACAGAACCAC-AAATTCTAACCAAGGCCAACAAGCCTAAGCATA---TAA-CTGACCCGGCCC--ACGCCGATCAACGAACCAAGTTACCCCGGGGATAACAGCGCTATCTTCTTCAAGAGTCCCTATCAACAAGAAGGTTTACGACCTCGATGTTGGATCAGGACACCCAAATGGTGCAGCCGCTATTAAAGGTTCGTTTGTTCAACGATT"
m_capensis_seq  = "TTGTCTTCTAAATAAAGACCTGTATGAACGGCTAAATGAGGATAAACCTGTCTCTTATAACCAACCAGTGAAACTGATCTCCCAGTACAAAAGCTGGAATCAACCCATAAGACGAGAAGACCCTGCGGAGCTTAAAACAAACCACTAATTAATATC-----ATCTT---AACCCTAGTGAAATGTTTTCAGTTGGGGCGACTTCGGAATAAAACACAACTTCCGAGCACAGAACCACT-AATTCTAACCAAGGCCAACAAGCCAAAGTATAA--TA---TGACCCGGCAC--ATGCCGATCAACGAACCAAGTTACCCCAGGGATAACAGCGCTATCCTCTTCAAGAGTCCCTATCAACAAGAGGGTTTACGACCTCGATGTTGGATCAGGACACCCAAATGGTGCAGCCGCTATTAAAGGTTCGTTTGTTCAACGATT"
m_vittata_seq   = "TTGTCTTCTAAATAAAGACCAGTATGAACGGCTAAATGAGGACAAACCTGTCTCTTATAATTAATCAGTGAAACTGATCTCCCAGTACAAAAGCTGGGATATTAACATAAGACGAGAAGACCCCGTGGAGCTTGAAAT-AAACCACTAAACAATAC--GTG----CCACTAGTTTA-TGTACTATTTTCAGTTGGGGCGACTTCGGAACAAAACAAAACTTCCGAGCACAGAACCAC-TTCCTCTAACCAAGGCCAACAAGCCTAAGACTC---ATAAACGACCCGGCCCACTTGCCGATCAACGAACCAAGTTACCCCGGGGATAACAGCGCTATCTTCTTCAAGAGTCCCTATCAACAAGAAGGTTTACGACCTCGATGTTGGATCAGGACACCCAAATGGTGCAGCCGCTATTAAAGGTTCGTTTGTTCAACGATT"

# Systemparameter (Einstellungen)

dna_map = { # maps the dna sequences above with a string identifier in a dictionary (not necessary but nice to have to automatically identify the correct dataset for subsequent processing steps)
    "Mabuya agilis": m_agilis_seq,
    "Mabuya atlantica": m_atlantica_seq,
    "Mabuya capensis": m_capensis_seq,
    "Mabuya vittata": m_vittata_seq
}

pickers = ["A", "T", "G", "C", "-"] # defines the dna sequence elements that are to be analysed

key_a = "Mabuya capensis" # defines DNA 1
key_b = "Mabuya vittata" # defines DNA 2

# Variablen

counter = 0 # saves number of characters in string during sequence analysis below (Auswertung Einzelbasen)
length_check = False # saves whether the compared strings have the same length
length = 0 # saves the length of the compared dna sequences

comparisons = 0 # saves number of comparisons during dna sequence comparison
similarities = 0 # saves number of similarities during dna sequence cmparison

# Auswertung Einzelbasen DNA 1

print(20 * "-") # within print() you can use math operators to manipulate strings
print()

print(key_a)

for picker in pickers: # iterates over the pickers list
    sequence = dna_map[key_a] # defines dna sequence according to dna_map and associated identifier (manually selected in key_a variable)

    for i in range(0, len(sequence)):
        if sequence[i] == picker:
            counter += 1

    print(f"{picker}: {counter}")

    counter = 0

print(f"Anzahl Elemente : {len(sequence)}")

# Auswertung Einzelbasen DNA 2

print()
print(20 * "-")
print()

print(key_b)

for picker in pickers:
    sequence = dna_map[key_b]

    for i in range(0, len(sequence)):
        if sequence[i] == picker:
            counter += 1

    print(f"{picker}: {counter}")

    counter = 0

print(f"Anzahl Elemente : {len(sequence)}")

print()
print(20 * "-")
print()

# Längenvergleich DNA 1 - DNA 2

if (len(dna_map[key_a]) == len(dna_map[key_b])):
    print("Die beiden Sequenzen haben dieselbe Länge.")
    length_check = True # saves boolean value for later reference
    length = len(dna_map[key_a]) # saves length of string for later reference
else:
    print("Die Sequenzen müssen dieselbe Länge haben.")

# Sequenzvergleich DNA 1 - DNA 2

sequence_a = dna_map[key_a] # saves dna_map[key_a] in new variable improve readability and reduce hirarchy in dictionary
sequence_b = dna_map[key_b]

if length_check:
    for i in range(0, length):
        if sequence_a[i] != "-" and sequence_b[i] != "-": # checks if either sequence_a or sequence_b contain "-" at given position, if yes skips to next character
            comparisons += 1

            if sequence_a[i] == sequence_b[i]: # checks if sequence_a or sequence_b have similar character at given position
                similarities += 1
            
# Prozentuale Übereinstimmung DNA 1 - DNA 2

similarity = similarities / comparisons

print()
print(20 * "-")
print()

print(f"{key_a} vs. {key_b}")
print("Die beiden Sequenzen haben dieselbe Länge")
print(f"Anzahl Vergleiche: {comparisons}")
print(f"Anzahl Treffer: {similarities}")
print(f"Übereinstimmung: {similarity}")

print()
print(20 * "-")
print()

# %%
