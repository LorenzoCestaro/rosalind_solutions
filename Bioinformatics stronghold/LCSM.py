# FASTA INPUT PARSING

filename = raw_input("Insert the name of the input file:")
fasta_input = "".join(open(filename))
sequences = fasta_input.strip(">").split(">")
seq_array = []

for i in range(0, len(sequences)):
    fasta_seq = list(sequences[i].split("\n"))
    fasta_seq = list("".join(fasta_seq[1:]))
    seq_array.append(fasta_seq)

# MOVING SHORTEST SEQUENCE TO THE TOP OF THE LIST

seq_array = sorted(seq_array, key=len)
    
# GENERATOR OF FIXED LENGTH POSSIBLE SUBSETS

def subseq(seq, subseq_length):
    possibleStartPositions = len(seq) - subseq_length + 1
    result = []
    
    for start in range(0, possibleStartPositions):
        result.append(seq[start:subseq_length+start])

    return result

# SUBSTRINGS COMPARISONS
longest_common_subs = []

for length in range(len(seq_array[0]), 0, -1):
    
    subsequences = subseq(seq_array[0], length)
    
    for sub_seq in subsequences:
        for seq in seq_array[1:]:
            if "".join(sub_seq) not in "".join(seq):
                break
        else:
            longest_common_subs.append("".join(sub_seq))

    if longest_common_subs != []:
        break

# PRINT LONGEST COMMON SUBSTRINGS

for i in longest_common_subs:
    print i    
