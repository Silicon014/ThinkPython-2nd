def is_power(a, b):
    if a == b:
        return True
    elif a % b == 0:
        if is_power(a / b, b):
            return True
        else:
            return False
    else:
        return False


def main():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(is_power(a, b))


main()
