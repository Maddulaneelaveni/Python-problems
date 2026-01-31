# Hallow pyramid pattern

n = int(input("Enter number of rows: "))
for i in range(1, n + 1): # for each row
    for j in range(n - i): # print leading spaces
        print(" ", end="")# print spaces
    for j in range(1, 2 * i):# print stars and spaces
        if j == 1 or j == 2 * i - 1 or i == n:# conditions for stars in determining hollow parts    
            print("*", end="")# print star
        else:
            print(" ", end="")# print space
    print()

