from reverseComplement import reverseComplement # script to compute the reverse complenment of a DNA string

# Parse FASTA input file consisting of a single sequence

filename = input("Insert the name of the input file:")
sequence = open(filename, 'r').readlines()[1:]
sequence = "".join(sequence).replace("\n", "")
rev_sequence = reverseComplement(sequence)[::-1] # this string is reversed to allow
                                                 # comparison with the same index values

output = []

for i in range(4, 13, 2):
    for j in range(0, len(sequence)-i+1):
        if j==0:
            if sequence[j:j+i] == rev_sequence[j+i-1::-1]:
                output.append([1, i])
        else:
            if sequence[j:j+i] == rev_sequence[j+i-1:j-1:-1]:
                output.append([j+1, i])

for i in output:
    print(str(i[0]) + " " + str(i[1]))
