# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.


def factoral_of_number(n):
    factoral = 1
    for i in range(1, n + 1):
        factoral *= i
    return factoral


print(factoral_of_number(5))