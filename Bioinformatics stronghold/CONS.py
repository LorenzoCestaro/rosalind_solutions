# reading input file
filename = raw_input("Insert the name of the input file:")
fasta_input = "".join(open(filename))
sequences = fasta_input.strip(">").split(">")

# initializing lists
seq_list = []
profile_matrix = [["A:", ], ["C:", ], ["G:", ], ["T:", ]]
consensus = []

# extracting sequences from input file, getting rid of descriptions.
# a multidimensional list is created:
# a list of lists(i.e. sequences) of nucleotides
for i in range(0, len(sequences)):
    seq = list(sequences[i].split("\n"))
    seq_list.append(list("".join(seq[1:])))

# nested loop for counting occurrences of a nucleotide
# at each position of the input sequences.
# results are stored in a multidimensional list.

for j in range(0, len(seq_list[0])):
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    for i in range(0, len(seq_list)):
        if seq_list[i][j] == "A":
            countA += 1
        if seq_list[i][j] == "C":
            countC += 1
        if seq_list[i][j] == "G":
            countG += 1
        if seq_list[i][j] == "T":
            countT += 1

    profile_matrix[0].append(countA)
    profile_matrix[1].append(countC)
    profile_matrix[2].append(countG)
    profile_matrix[3].append(countT)

# creating consensus sequence by looping through rows in every column,
# more frequent nucleotide is found by retrieving the index of the maximum
# value in a temporary list. Each index represents a different nucleotide.
for j in range(1, len(profile_matrix[0])):
    temp_list = []
    for i in range(0, len(profile_matrix)):
        temp_list.append(profile_matrix[i][j])
    index = temp_list.index(max(temp_list))
    if index == 0:
        consensus.append("A")
    if index == 1:
        consensus.append("C")
    if index == 2:
        consensus.append("G")
    if index == 3:
        consensus.append("T")

# printing matrix and consensus:
print "".join(consensus)

for i in range(0, len(profile_matrix)):
    for j in range(0, len(profile_matrix[0])):
        print profile_matrix[i][j],

    print "\n"
    
