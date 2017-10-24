def read(fruit):
    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print(letter, end="")
        index = index + 1


def ducklings():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)


def main():
    word = input("enter a word: ")
    print("it is")
    read(word)


ducklings()
