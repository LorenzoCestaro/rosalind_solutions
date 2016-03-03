# FASTA INPUT PARSING

filename = raw_input("Insert the name of the input file:")
fasta_input = "".join(open(filename))
sequences = fasta_input.strip(">").split(">")
seq_array = []
adj_list = []

for i in range(0, len(sequences)):
    seq = list(sequences[i].split("\n"))
    seq = [seq[0], list("".join(seq[1:]))]
    seq_array.append(seq)


# COMPUTING ADJACENCIES

for i in range(len(seq_array)):

    for j in range(len(seq_array)):

        if seq_array[i][1] != seq_array[j][1]:
            if seq_array[i][1][-1] == seq_array[j][1][2]:
                if seq_array[i][1][-2] == seq_array[j][1][1]:
                    if seq_array[i][1][-3] == seq_array[j][1][0]:
                        adj_list.append(str(seq_array[i][0] + " " + seq_array[j][0]))

# PRINTING ADJACENCIES

for i in range(len(adj_list)):
    print adj_list[i] + "\n",
