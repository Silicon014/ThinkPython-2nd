def gcd(a, b):
    if b == 0 or a == 0:
        return a + b
    elif a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)


def main():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print("the gcd of a and b is", end=" ")
    print(gcd(a, b))


main()
