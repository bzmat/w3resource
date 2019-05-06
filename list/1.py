# write a Python program to sum the items of list.

def sum_list(list):
    sum_numbers = 0
    for i in list:
        sum_numbers = sum_numbers + i
    return sum_numbers


print(sum_list([2,3,5,1]))
