# Write a Python program to print the even numbers from a given list.

def find_even(datalist):
    even_list = []
    for i in datalist:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


print(find_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
