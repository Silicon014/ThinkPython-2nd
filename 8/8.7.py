def count(word, char):
    counter = 0
    for letter in word:
        if letter == char:
            counter = counter + 1
    return counter


def main():
    fruit = 'tomato'
    a = count(fruit, 'o')
    print(a)


main()
