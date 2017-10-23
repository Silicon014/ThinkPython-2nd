def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


# 假装这是palindrome.py
def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1] and is_palindrome(word[1:-1]):
        return True
    else:
        return False


def main():
    print(is_palindrome(input("enter a word. It will return whether it's palidrome. word: ")))


main()
