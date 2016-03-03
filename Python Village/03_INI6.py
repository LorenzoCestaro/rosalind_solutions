text = raw_input("Insert text to analyze:")

word_count = {}

for word in text.split(" "):
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print key,
    print value
