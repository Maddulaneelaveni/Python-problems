# Mirrored star rhombus pattern

#     *****
#   *****
#  *****
# *****
#*****
# *****
#  *****
#   *****
#    *****

n = 5
# Upper part
for i in range(n):
    print(" " * (n - i - 1) + "*" * n)
# Lower part
for i in range(1, n):
    print(" " * i + "*" * n)

