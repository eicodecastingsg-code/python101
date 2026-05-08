# introduce a function that can hold ANY number of parameters
# use * to make it a special parameter

def adder(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(result)



adder(67, 67)
adder(67, 67, 67)
adder(67, 67, 67, 67)
adder(67, 67, 67, 67, 67)