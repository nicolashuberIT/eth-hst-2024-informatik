# %%

# var

dna = "ATCCTATCGAT"
seq = "A"

counter = 0
positions = []

# logic

for i in range(0, len(dna)): # len(dna) returns the number of characters within the `dna` string and thus sets the proper upper limit for this loop
    if dna[i] == seq:
        counter += 1 # += adds the given value to the variable
        positions.append(i)

# logs

print(f"DNA: {dna}") # f strings can be used to bring dynamic content into strings
print(f"Sequence: {seq}")
print()
print(f"Sequence found n times in DNA: {counter}")
print(f"Sequence found at positions: {positions}")
# %%
