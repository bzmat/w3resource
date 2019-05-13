# Write a Python function to check whether a number is in a given range.

def find_in_range(number, start, end):
 if number in range(start, end + 1):
    return True
 else:
    return False


print(find_in_range(0, 1 ,10))
