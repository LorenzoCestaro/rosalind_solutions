filename = raw_input("Insert the name of the input file:")
fasta_input = "".join(open(filename))
sequences = fasta_input.strip(">").split(">")
seq_2Dlist = []
seq_GC_contents = []

for i in range(0, len(sequences)):
    seq = list(sequences[i].split("\n"))
    seq = [seq[0], "".join(seq[1:])]
    seq_2Dlist.append(seq)

for i in range(0, len(seq_2Dlist)):
    seq = list(seq_2Dlist[i][1])
    countGC = 0
    countTot = 0

    for j in range(0, len(seq)):
        if seq[j] == "G" or seq[j] == "C":
            countGC += 1
            countTot +=1
        else:
            countTot += 1

    GC_content = float(countGC)/float(countTot) * 100
    seq_2Dlist[i].append(GC_content)

GC_contents = [seq_2Dlist[i][2] for i in range(len(seq_2Dlist))]

print seq_2Dlist[GC_contents.index(max(GC_contents))][0], max(GC_contents)
