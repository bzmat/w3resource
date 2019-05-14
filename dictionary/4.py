# write a Python script to check if a given key already exist in dictionary.

def find_in_dict(d, key):
    if key in d:
        print("Key is present in the dictionary")
    else:
        print("Key is not present in the dictionary")


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

find_in_dict(d,2)