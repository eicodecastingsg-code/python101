# Loop Controls (break, continue)

# break - terminates the loop immediately


# build a countdown timer that stops when it hits 50
import time
for i in range(60, 0, -1):
    print(i)
    time.sleep(0)
    if i == 50:
        print("loop killed")
        break


# given a list, sum its elements from left to right and stop when the sum exceeds 100
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
total = 0
for i in range(0, len(nums), 1):
    total += nums[i]
    if total > 100:
        print(f"sum exceeded 100, loop killed. sum = {total}")
        break


# given a list, search for a target number. Stop searching when it is found.
# the target number is 67
# use a for-each loop
x = [123, 90, 67, 3, 1, 48, 99, 100, 78, 8]

index = 0
for n in x:
    if n == 67:
        print(f"target found, it is located at position {index}")
        break
    index += 1
else:
    print("target number does not exist in the list")



"""
In a for-else loop, the else clause will only be executed if the for loop does not hit "break"
"""

























