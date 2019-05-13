# Write a Python function to check whether a number is perfect or not.


def find_ideal(n):
    new_list = []
    for i in range(1, n):
        if n % i == 0:
            new_list.append(i)
    sum_new_list = 0
    for j in new_list:
        sum_new_list += j
    if sum_new_list == n:
        print("Liczba", n, "jest liczbą doskonałą")
    else:
        print("Liczba", n, " nie jest liczbą doskonałą")


find_ideal(28)