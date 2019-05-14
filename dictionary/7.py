# write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are squers of key

d = {}
for i in range(1, 16):
    d.update({i: i**2})

print(d)