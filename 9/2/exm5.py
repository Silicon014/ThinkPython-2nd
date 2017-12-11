def uses_all(word, string):
    for letter in word:
        if (letter in string) == False:
            return False
    return True

def aeiou(string):
    return uses_all('aeiou', string)

def aeiouy(string):
    return uses_all('aeiouy', string)

def test(func):
    x = 0
    y = 0
    a = open("words.txt")
    for line in a:
        if func(line) == True:
            x += 1
        else:
            pass
        y += 1
    return x / y

print(test(aeiou))
print(test(aeiouy))
