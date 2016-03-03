s = raw_input("Insert nucleotide sequence:")
s.upper()

countA = 0
countC = 0
countG = 0
countT = 0

for c in s:
    if c == "A":
        countA += 1
    elif c == "C":
        countC += 1
    elif c == "G":
        countG += 1
    elif c == "T":
        countT += 1
    else:
        print "Invalid nucleotides symbols are present in the sequence"

print countA,
print countC,
print countG,
print countT
