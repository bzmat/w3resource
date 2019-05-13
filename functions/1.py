# Write a Python function to find the Max of three numbers
def find_max(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z


print(find_max(5, 6, 5))
