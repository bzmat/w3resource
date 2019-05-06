# write a Python program to calculate the length of string

def string_lenght(string):
    count = 0
    for char in string:
        count += 1
    return count


def string_lenght2(string):
    len_str = len(string)
    return len_str

# test
print(string_lenght("mateusz"))
print(string_lenght2("mateusz"))