def prot_translate(seq):
	gencode = {
			'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
			'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
			'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
			'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
			'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
			'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
			'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
			'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
			'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
			'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
			'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
			'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
			'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
			'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
			'UAC':'Y', 'UAU':'Y', 'UAA':'*', 'UAG':'*',
			'UGC':'C', 'UGU':'C', 'UGA':'*', 'UGG':'W'}

	protein = []

	for i in range(0, len(seq), 3):
		if(i<=len(seq)-3):
			codon = seq[i] + seq[i+1] + seq[i+2]
			protein.append(gencode[codon])
		else:
			protein.append('?')

	return "".join(protein)



