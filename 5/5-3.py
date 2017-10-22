def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
if is_triangle(a, b, c):
    print("Yes")
else:
    print("No")