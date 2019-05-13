# write a Python program that prints each item and its corresponding type the following list


def type_of_element(datalist):
    for element in datalist:
        print("Type of", element, "is", type(element))



datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

type_of_element(datalist)