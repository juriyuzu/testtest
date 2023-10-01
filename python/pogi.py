import os
a = input()
b = input()

x = len(a)
y = len(b)

os.system('cls')
print()
for i in range(x):
    for j in range(x - i):
        print(a[j], end = '')
    print()

for i in range(y - 1, -1, -1):
    for j in range(y - i):
        print(b[j], end = '')
    print()