# Functions and Arguments

# Question 1
def greet(name, age):
    print(f"{name} is {age} years old")


# Question 2
def subtract(a, b):
    return a - b


# Question 3
def power(base, exponent=2):
    return base ** exponent


# Question 4
def calculate(price, tax=0.1):
    return price + (price * tax)


# Question 5
def printNames(*names):
    print(names[2])


# Question 6
def add_item(item, container):
    container.append(item)
    print(container)


# Question 7
def mod(*blocks):
    print(blocks[0][0] + blocks[1][1] + blocks[2][2])


# Question 8
def build(*nums):
    maximum = 0
    for i in nums:
        if i > maximum:
            maximum = i
    print(maximum)


# Question 9
def join(x, y, z):
    print(x[0:2:] + y[2:4:] + z[::])

join(['a', 'b', 'c', 'd', 'e'], ['$', '#', '%', '*', '^', '@'], [1, 2, 3])




























