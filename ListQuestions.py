# Q1
# define a function that returns the sum of all elements in a list
def sum_list(L):
    total = 0
    for i in range(0, len(L), 1):
        total = total + L[i]
    return total


# Q2
# Find the maximum element of a list
def max_in_list(L):
    current_max = L[0]
    for i in range(1, len(L), 1):
        if L[i] > current_max:
            current_max = L[i]
    print(current_max)



# Q3
# Count how many numbers are even and how many are odd
def count_even_odd(L):
    odd_count = 0
    even_count = 0

    for n in L:
        if n % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1

    print(f"Odd numbers: {odd_count}")
    print(f"Even numbers: {even_count}")


count_even_odd([23, 34, 54, 6, 57, 76, 2, 100])



# Q4
# Print in 1 line all elements that are greater than the average
def print_above_average(L):
    average = sum_list(L) / len(L)
    for n in L:
        if n > average:
            print(n, end=" ")
    print()

print_above_average([3, 4, 5, 6, 7, 8, 9, 10])




# Q5
# Check if a list is sorted in ascending order
def is_sorted(L):
    for i in range(1, len(L), 1):
        if L[i] < L[i - 1]:
            return False
    return True

print(is_sorted([2, 3, 100, 5, 6]))




# Q6
# print all local peaks of a list
# a local peak is a number that is greater than its neighbours
def find_local_peaks(L):
    for i in range(1, len(L) - 1, 1):
        if L[i] > L[i - 1] and L[i] > L[i + 1]:
            print(f"A local peak: {L[i]}")


find_local_peaks([5, 100, 2, 200, 5, 300, 6])












































