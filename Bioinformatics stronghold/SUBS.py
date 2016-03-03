string = list(raw_input("Insert nucleotide sequence:"))
substring = list(raw_input("insert substring to be found:"))
output = list()

for i in range(len(string)-len(substring)+1):
    if string[i] == substring[0]:
        if "".join(string[i:i+len(substring)]) == "".join(substring):
            output.append(str(i+1))

print " ".join(output)
print len(output)
