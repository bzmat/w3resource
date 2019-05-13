# Write a Python function that accepts a string and calculate the number of upper case letters
# and lower case letters.

def lower_or_upper(string):
    lower = 0
    upper = 0
    for i in string:
        if i.islower() == True:
            lower += 1
        elif i.isupper() == True:
                upper += 1
    print("No. of Lower case characer:", lower)
    print ("No. of Upper case characer:", upper)


lower_or_upper('The quick Brow Fox')