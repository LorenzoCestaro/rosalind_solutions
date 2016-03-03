a = int(raw_input("Type first integer:"))
b = int(raw_input("Type second integer:"))
odds = []

for i in range(a, b+1):
    if i % 2 == 1:
        odds.append(i)

print sum(odds)
