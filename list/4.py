# write a Python program to get the smallest number from the list

def smalles_number(ithem):
    small = ithem[0]
    for element in ithem:
        if element < small:
            small = element
    return small


print(smalles_number([2, -1, 3, 5]))
