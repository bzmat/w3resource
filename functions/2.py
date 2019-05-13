# Write a Python function to sum all the numbers in a list.

def sum_list(datalist):
    sumOf = 0
    for i in datalist:
        sumOf += i
    return sumOf


print(sum_list((8, 2, 3, 0, 7)))