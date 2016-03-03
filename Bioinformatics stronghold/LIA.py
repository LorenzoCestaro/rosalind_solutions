import math

def independent_alleles(k, N):
    n_AaBb = int(N)
    pop = 2**k
    prob = []

    while n_AaBb <= pop:
        # Calculate possible orderings of genotypes
        comb = math.factorial(pop)/(math.factorial(pop-n_AaBb)*math.factorial(n_AaBb))
        # Calculate probability of occurence of a number of AaBb
        # in the total population. Accounting for all possible arrangements.
        # Append the result to the probabilities array.
        prob.append((0.25**n_AaBb * 0.75**(pop-n_AaBb))*comb)
        # Increment the number of AaBb genotipes to calculate probabilities for
        # all the scenarios with more AaBb genotypes than the provided N argument
        n_AaBb = n_AaBb+1

    # Sum over the prob array to return the overall probability of having AT LEAST
    # N AaBb genotypes at the k generation
    return sum(prob)
