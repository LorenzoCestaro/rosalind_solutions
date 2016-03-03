def DNAtoRNA(seq):
	
	for c in range(len(seq)):
			if seq[c] == "T":
					seq[c] = "U"

	return "".join(seq)

