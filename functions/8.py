# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def find_uniq(datalist):
    new_list = []
    for i in datalist:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(find_uniq([1, 2, 3, 3, 3, 3, 4, 5]))