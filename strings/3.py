# write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the strinf length is less than 2, return instead of empty string.

def first_and_last(string):
    if len(string) < 2:
        new_string = ""
    else:
        new_string = string[0] + string[1] + string[-2] + string[-1]
    return new_string

# test
print(first_and_last("mateusz"))
print(first_and_last("wc"))
print(first_and_last("m "))


