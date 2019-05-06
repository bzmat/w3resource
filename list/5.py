# write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are the same from the given list of strings.

def count_strings(listStrings):
    for element in listStrings:
        if len(element) >= 2:

            for letter in element:
                count = 0
                if element[0] == element[-1]:
                    count = count + 1
    return count




print(count_strings(['abc', 'xyz', 'aba', '1221']))