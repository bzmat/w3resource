# Write a Python program to sort (ascending and descending) a dictionary by value.
from operator import itemgetter

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print(d)

print(sorted(d.items(), key=itemgetter(-1)))


print(sorted(d.items(), key=itemgetter(-1), reverse=True))

