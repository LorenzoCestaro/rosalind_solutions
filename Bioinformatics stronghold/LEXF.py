from itertools import product

filename = input("Insert the name of the input file:")
alphabet = open(filename).readlines()[0]
w_len = open(filename).readlines()[1]

alphabet = alphabet.replace(" ", "").replace("\n", "")
w_len = int(w_len)

w_list = product(alphabet, repeat = w_len)

for i in w_list:
    i = str(i).replace("(", "").replace(")", "").replace(", ", "").replace("'", "")
    print(i)
