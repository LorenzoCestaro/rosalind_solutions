# DICTIONARY WITH TOTAL NUMBER OF CODON CODING A CERTAIN AA
codons_per_aa = {
    'I':3, 'M':1, 'T':4, 'N':2, 'K':2,
    'S':6, 'R':6, 'L':6, 'P':4, 'H':2,
    'Q':2, 'V':4, 'A':4, 'D':2, 'E':2,
    'G':4, 'F':2, 'Y':2, 'C':2, 'W':1,
    '*':3}

# CUSTOM PROD() FUNCTION
def prod(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

# FUNCTION COMPUTING NUMBER OF POSSIBLE MRNA ORIGINAL SEQUENCES (MODULED BY 1M)
def mrna_combinations(prot_seq):
    
    for i in range(len(prot_seq)):
        prot_seq[i] = codons_per_aa[prot_seq[i]]

    prot_seq.append(codons_per_aa['*'])

    return prod(prot_seq)%1000000


prot_seq = list(raw_input("Insert protein sequence to reverse translate:"))

print mrna_combinations(prot_seq)
