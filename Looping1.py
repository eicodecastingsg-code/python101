# for-loop
# 1. range-based for loop (loops through a range of integers)
# 2. for-each loop (loops through a collection eg, list, string)

# Exercise 1: print all numbers from 1 to 10
for i in range(1, 11, 1):
    print(i, end=" ")
print("\n")


# Exercise 2: loop through a list using a range-based for loop
x = [1000, 2000, 3000, 4000, 5000]
for i in range(0, 5, 1):
    print(x[i], end=" ")
print("\n")


# Exercise 3: print all elements in a list backward
x = [1000, 2000, 3000, 4000, 5000]
for i in range(4, -1, -1):
    print(x[i], end=" ")
print("\n")


# Exercise 4: loop through a string with a for-each loop
name = "Lady-Gaga"
for i in name:
    print(i, end=" ")
print("\n")


# Exercise 5: loop through a list with a for-each loop
y = ["jovan", "youwei", "ruize", "jaden", "eros"]
for n in y:
    print(n)
print("\n")


# Exercise 6: loop through a string and print all the vowels
food = "pizza"
vowels = "aeiouAEIOU"

for char in food:
    if char in vowels:
        print(char)


print("\n")

# Exercise 7: loop through a list and sum all its elements
nums = [5, 2, 9, 67, 100]
total = 0
for i in range(0, len(nums), 1):
    total += nums[i]
print(total)



























