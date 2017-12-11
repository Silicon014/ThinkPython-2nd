def has_no_ch(word, ch):
    if ch in word:
        return False
    else:
        return True

def words_no_ch(fi, ch):
    no_ch = 0
    total = 0
    for line in fi:
        if has_no_ch(line.strip(), ch):
            no_ch += 1
        total += 1
    return no_ch / total

def all_percentage():
    for i in range(26):
        fi = open("words.txt")
        num = ord('a') + i 
        char = chr(num)
        print(char + ':', end='')
        print(words_no_ch(fi, char))

def answer():
    fi = open("words.txt")
    def has_no_e(word):
        re = has_no_ch(word, 'e')
        if re == True:
            print(word)
            return re
        else:
            return re

    def words_no_e(fi):
        a = 0
        b = 0
        for line in fi:
            if has_no_e(line.strip()):
                a += 1
            else:
                pass
            b += 1
        return a / b

    r = words_no_e(fi)
    print("e: " + str(r))

answer()
