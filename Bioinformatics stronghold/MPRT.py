import urllib2

# FUNCTION THAT GENERATES PROTEIN FASTA URL GIVEN THE RELATIVE ID
def uniprot_url_generator(prot_id):
    return str("http://www.uniprot.org/uniprot/" + prot_id + ".fasta")

# PARSING INPUT FILE WITH IDs OF PROTEINS TO BE ANALIZED
filename = raw_input("Insert name of the file containing uniprot IDs:")
input_file = open(filename).read().split("\n")

# RETRIEVING SEQUENCES FROM UNIPROT SERVERS BY ID
for line in input_file:
    print uniprot_url_generator(line)
    prot_seq = urllib2.urlopen(uniprot_url_generator(line))
    prot_seq = prot_seq.read().split("\n")
    prot_seq = "".join(prot_seq[1:])
    prot_seq = list(prot_seq)

    # SCANNING SEQUENCES FOR REQUESTED PATTERN
    pattern_pos = []
    for aa in range(len(prot_seq)):
        if prot_seq[aa] == "N":
            if prot_seq[aa+1] != "P":
                if prot_seq[aa+2] == "S" or prot_seq[aa+2] == "T":
                    if prot_seq[aa+3] != "P":
                        pattern_pos.append(str(aa+1)) #aa positions start at 1 index
        else:
            continue
        

    if pattern_pos != []:
        print line
        print " ".join(pattern_pos)

