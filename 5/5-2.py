def check_fermat(a, b, c, n):
    if a ** n + b ** n == c ** n:
        return True
    else:
        return False
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
n = int(input("enter n: "))
if n <= 2:
    print("n <= 2")
else:
    if check_fermat(a, b, c, n):
        print("ferm is wrong!")
    else:
        print("No,it doesn't work")
