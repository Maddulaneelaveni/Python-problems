# Rectangle Pattern

# *********
# *********
# *********
# *********
# *********

rows = 4
cols = 6

for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()


# Another way to print Rectangle Pattern

rows = 4
cols = 6

for i in range(rows):
    print("*" * cols)
    print()
    