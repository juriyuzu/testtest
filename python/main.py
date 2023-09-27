def main():
    x = int(input("Type an integer: "))
    print()
    
    a = 1
    for i in range(x):
        print(' ' * (x + 1 - i) + '*' * a)
        print(' ' * (x - i) + '*' * (a + 2))
        print(' ' * (x - 1 - i) + '*' * (a + 4))
        a += 2



print("\n\n")

main()

print("\n\n")
