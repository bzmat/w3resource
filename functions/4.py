# Write a Python program to reverse a string.

def reverse_string(string):
    for i in range(len(string) - 1, -1, -1):
        print(string[i], end="")


reverse_string("1234abcd")