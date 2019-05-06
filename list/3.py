# write a Python program to get the largest number from the list


def largest_element(ithems):
    large = ithems[0]
    for element in ithems:
        if element > large:
            large = element
    return large


print(largest_element([2, 6, 5, 1, -10]))

