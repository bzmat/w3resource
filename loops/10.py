# write a Python program which iterates the integers from 1 to 50. For multiples if three print "Fizz"
# instead of the number and for the multiples of five print "Buzz". For number which are multiples of both three
# and five print "FizzBuzz"

def change_number(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

start = 1
end = 50

change_number(start, end)