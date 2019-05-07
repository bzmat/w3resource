# write a Python program that accept a word from the user and reverse it.

def revers_word(string):
    new_word = ""
    for i in range(len(string) -1, -1, -1):
        new_word = new_word + string[i]
    print(new_word)


# test
string = input("Podaj słowo do odwórócenia: ")

revers_word(string)
