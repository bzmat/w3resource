# Write a Python function to multiply all the numbers in a list.

def multiply_of_number(datalist):
    multiply = 1
    for i in datalist:
        multiply *= i
    return multiply


print(multiply_of_number((8, 2, 3, -1, 7)))