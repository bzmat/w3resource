# Write a Python function that takes a number as a parameter and check the number is prime or not

def find_prime(n):
    if n <= 1:
        print("Zmień parametr")
    elif n > 3 and (n % 2 == 0 or n % 3 == 0):
        print("Liczba", n, "nie jest liczą pierwszą")
    else:
        print("Liczba", n, "jest liczbą pierwszą")


find_prime(7)