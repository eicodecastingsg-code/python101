# The Set Data Structure
# Declared with a {}
# It can only store unique elements (no duplicated elements allowed)
# It does not maintain elements order

x = {10, 20, 30, 30, 30, 40, 50}
print(x)


# Cannot access elements in a set by index
# print(x[0]) -> error


# loop though a set with for-each loop
for i in x:
    print(i)