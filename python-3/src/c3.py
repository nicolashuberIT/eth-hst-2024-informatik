# %%

# var

dna = "ATCATGAGGGCCTATCTA"
seq = ["A","T","G","AT","ATG"]

counter = 0
positions = []

# logic

for i, picker in enumerate(seq): # iterates through the seq list, the list elements being assigned to the picker variable during each iteration
    for j in range(len(dna)):
        if dna[j:j + len(picker)] == picker:
            counter += 1
            positions.append(j)

    print(f"DNA: {dna}")
    print(f"Sequence: {picker}")
    print(f"Sequence found n times in DNA: {counter}")
    print(f"Sequence found at positions: {positions}")
    print()

    # reset

    counter = 0
    positions = []

# %%
