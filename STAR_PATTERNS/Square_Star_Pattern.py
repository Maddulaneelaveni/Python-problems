# Square Star Pattern

# *****
# *****
# *****
# *****
# *****


n = int(input("Enter a number: ")) # size of the square
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

# Alternative simpler version without nested loops using string multiplication 
# string multiplication means repeating a string multiple times by multiplying it with an integer.

n = 5
for i in range(n):
    print("*" * n)


