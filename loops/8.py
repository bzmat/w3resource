# write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# use "continue" statement


def print_numbers(datalist):
    for element in datalist:
        if element == 3 or element == 6:
            continue
        print(element)



#test
print_numbers([0, 1, 2, 3, 4, 5,6])
