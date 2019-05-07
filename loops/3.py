# write a Python program to guess a number between 1 to 9. User is promped to enter a guess.
# If the user guesses the wrong then the prompt appears again until the guess is correct, on successful guess, user
# will get a "Well guessed!" message, and the program will exit.

import random

computer_number = random.randint(1, 9)

user_number = ""

while user_number != computer_number:
   user_number = int(input("Podaj liczbe jaką wylosowałem: "))

print("Well guess")

