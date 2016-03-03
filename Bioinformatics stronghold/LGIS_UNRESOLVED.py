# Parsing input

filename = input("Insert the name of the input file:")
permutation = open(filename).readlines()[1]

permutation = permutation.replace(" ", "").replace("\n", "")
print(permutation)

best_inc_sub = []
best_dec_sub = []

# Longest common subsequence recursive algorithm

def lcs_len(x, y):
    """This function returns length of longest common sequence of x and y."""
 
    if len(x) == 0 or len(y) == 0:
        return 0
 
    xx = x[:-1]   # xx = sequence x without its last element    
    yy = y[:-1]
 
    if x[-1] == y[-1]:  # if last elements of x and y are equal
        return lcs_len(xx, yy) + 1
    else:
        return max(lcs_len(xx, y), lcs_len(x, yy))

# By passing as lcs_len() arguments the permutation and an ordered version of it
# we can compute the length of the longest increasing/decreasing subsequence

inc_permutation = sorted(permutation)
dec_permutation = inc_permutation[::-1]

print(lcs_len(permutation, inc_permutation))
print(lcs_len(permutation, dec_permutation))
