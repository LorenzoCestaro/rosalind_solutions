from PROT import prot_translate # prot_translate function to translate RNA into AA

# FASTA file parsing

filename = input("Insert the name of the input file:")
fasta_input = "".join(open(filename))
sequences = fasta_input.strip(">").split(">")
seq = ""
introns = []

for i in range(0, len(sequences)):
    sequence = list(sequences[i].split("\n"))
    sequence = "".join(sequence[1:])
    if i==0:
        seq = sequence
    else:
        introns.append(sequence)

# Removing introns from the main sequence

for i in range(len(introns)):
    seq = seq.replace(introns[i], "")

# Translating sequence into RNA and into AAs

seq = seq.replace("T", "U")
seq = prot_translate(seq)

print(seq)
