from itertools import permutations
import math

def gene_permutations(n):
    
    tot_perm = math.factorial(n)
    output = [tot_perm]

    # Generating vector of n different elements
    elem = []
    for i in range(1,n+1):
        elem.append(i)

    # Listing permutations with itertools
    perm_list = permutations(elem)

    for i in perm_list:
        i = list(i)
        output.append(str(i).replace("[", "").replace("]", "").replace(",", ""))

    return output

