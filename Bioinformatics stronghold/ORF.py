from PROT import prot_translate                 # prot_translate function to translate RNA into AA
from reverseComplement import reverseComplement # script to compute the reverse complenment of a DNA string

# Parse FASTA input file consisting of a single sequence

filename = input("Insert the name of the input file:")
sequence = open(filename, 'r').readlines()[1:]
sequence = "".join(sequence).replace("\n", "")
rev_sequence = reverseComplement(sequence)

# Translating to RNA

sequence = sequence.replace('T', 'U')
rev_sequence = rev_sequence.replace('T', 'U')


proteins = []

# Sequence scanning algorithm

def prot_finder(seq):
    for i in range(len(seq)):
        if seq[i] == 'M':
            for j in range(i, len(seq)):
                if seq[j] == '*':
                    proteins.append(seq[i:j])
                    break
    return proteins

# Iterating through the 3 reading frames for the sequence and it's reverse complement

for i in [0,1,2]:
    seq = sequence[i:]
    seq = prot_translate(seq)
    prot_finder(seq)
    rev_seq = rev_sequence[i:]
    rev_seq = prot_translate(rev_seq)
    prot_finder(rev_seq)

# Removing duplicates
proteins = list(set(proteins))

# Printing results

for i in proteins:
    print(i)


