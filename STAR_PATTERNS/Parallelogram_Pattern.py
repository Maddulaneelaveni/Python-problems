# Parallelogram Pattern
#     *****
#    *****
#   *****
#  *****


n = 5  # number of rows
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Print stars
    for k in range(n):
        print("*", end="")
    print()

# Alternative simpler version without nested loops using string multiplication
n = 5  # number of rows
for i in range(n):
    print(" " * (n - i - 1) + "*" * n)
    