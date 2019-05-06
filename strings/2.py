# write a Python program to count the number of characters in a string

def frequency_char(string):
    new_dict = {}
    for char in string:
        new_dict.update({char: string.count(char)})
    return new_dict

# test

print(frequency_char("google.com"))
