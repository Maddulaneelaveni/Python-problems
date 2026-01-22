# Hollow square star pattern
# *****
# *   *
# *   *
# *   *
# *****

n = int(input("Enter a number: ")) # size of the square
for i in range(n):
    for j in range(n):
        # Print star at the borders
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")  # Print space inside the square
    print()
