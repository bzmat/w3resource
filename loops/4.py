# write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = 5

for i in range(n):
    for j in range(i):
        print("* ", end="")
    print(" ")

for i in range(n, 0, -1):
    for j in range(i):
        print("* ", end="")
    print(" ")

sign = ""
for i in range(n):
    sign = "* " * i
    print(sign)

for i in range(n, 0, -1):
    sign = "* " * i
    print(sign)