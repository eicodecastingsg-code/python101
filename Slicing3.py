# LIST Slicing

x = [i for i in range(3, 31, 3)]
print(x)

# Q1: extract the last half of list x
mid = len(x) // 2
print(x[mid::])

# Q2: Slice list x into 5 equal chunks, and print them
for i in range(0, 9, 2):
    print(x[i:i+2:])


# Q3: Replace every chunk of size 2 with its sum
y = []
for i in range(0, 9, 2):
    y.append(x[i] + x[i + 1])
print(y)


# Q4: Print every sliding window of size 3
# x = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# output:
# [3, 6, 9]
# [6, 9, 12]
# [9, 12, 15]
# [12, 15, 18]
# [15, 18, 21]
# [18, 21, 24]
# [21, 24, 27]
# [24, 27, 30]




















