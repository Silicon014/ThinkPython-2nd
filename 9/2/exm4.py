def uses_only(words, string):
    for i in string.lower():
        if i in words.lower(): 
            pass
        elif i != ' ':
            return False
    return True

print(uses_only('acefhlo', 'Hoe alfalfa'))
