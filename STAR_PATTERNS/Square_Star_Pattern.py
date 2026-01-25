# Square Star Pattern

n = int(input("Enter a number: ")) # size of the square
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()


n = 5
for i in range(n):
    print("*" * n)

