filename = raw_input("Name of input file:")

inputfile = open(filename, "r")
outputfile = open("output.txt", "w")
inputfile_list = inputfile.readlines()

for i in range(0, len(inputfile_list)):
    if i % 2 == 1:
        outputfile.write(inputfile_list[i])

outputfile.close()

