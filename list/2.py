# write a Python program to multiplies all the items in a list.

def multi_list(items):
    mulit_numbers = 1
    for element in items:
        mulit_numbers = mulit_numbers * element
    return mulit_numbers


print(multi_list([2,4,6]))
