x = int(input("Enter a number: "))
a = 1
b = 0
c = 0
while x:
    print(a)
    c = b
    b = a
    a = b + c
    x -= 1