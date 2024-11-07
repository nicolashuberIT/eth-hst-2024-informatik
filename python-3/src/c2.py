# %%

# var

dna = "ATCCTATCGAT"
seq = "AT"

counter = 0
positions = []

# logic

for i in range(0, len(dna)):
    if dna[i:(i + len(seq))] == seq: # i:(i + len(seq)) slices the dna list to a new list that begins at indice i and ends before indice i + len(seq) (in this example seq contains a picker of length 2), the range will be automatically adjusted in case you change the seq variable
        counter += 1
        positions.append(i)

# logs

print(f"DNA: {dna}")
print(f"Sequence: {seq}")
print()
print(f"Sequence found n times in DNA: {counter}")
print(f"Sequence found at positions: {positions}")
# %%
