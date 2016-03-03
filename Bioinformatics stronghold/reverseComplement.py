def reverseComplement(sequence):

    s = list(sequence)
    
    for c in range(0,len(s)):
        if s[c] == "T":
            s[c] = "A"
        elif s[c] == "A":
            s[c] = "T"
        elif s[c] == "G":
            s[c] = "C"
        elif s[c] == "C":
            s[c] = "G"

    return "".join(s)[::-1]
