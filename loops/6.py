# write a Python program to count the number od even and odd numbers from a series of numbers.


def count_numbers(serie):
    total_even = 0
    total_odd = 0
    for i in serie:
        if i % 2 == 0:
            total_even += 1
        else:
            total_odd += 1
    print("Numbers of even numbers:", total_even)
    print("Numbers od odd numbers:", total_odd)


# test
count_numbers((1, 2, 3, 4, 5, 6, 7, 8, 9))