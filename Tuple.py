# The Tuple Data Structure
# Declared with a ()
# A tuple is immutable (cannot be changed)
# Any attempts to edit a tuple leads to an error!

a = (50, 40, 30, 20, 10)
# a[0] = 1000   -> error! not allowed to modify a tuple's data

# A tuple does maintain elements order
# hence, we can access tuple elements by index
print(a)
print(a[0])
print(a[1])


# A tuple can also be declared without ()
b = 100,
print(type(b))
print(b)


c = 200, 300, 400, 500
print(type(c))


# Although a tuple is immutable, we can combine multiple tuples
BIG = a + b + c
print(BIG)


























