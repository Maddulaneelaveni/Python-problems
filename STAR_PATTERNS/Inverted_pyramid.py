# Inverted Pyramid Star Pattern
# *********
#  *******
#   *****
#    ***
#     *
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    for space in range(n - i):
        print(" ", end="")
    for star in range(1, 2 * i):
        print("*", end="")
    print()
