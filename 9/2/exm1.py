fin = open("words.txt")
def print_by_len(fin, lenth):
    for line in fin:
        word = line.strip()
        if len(word) > lenth:
            print(word)

print_by_len(fin, 20)
