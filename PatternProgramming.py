# print a right angle triangle of asterisk
# hint: use string multiplication and looping

def right_angle_triangle(n):
    for i in range(1, n+1, 1):
        print("*" * i)



# print a right angle triangle of numbers
"""
1
22
333
4444
55555
666666

hint: str(), string multiplication, looping
"""
def number_triangle(n):
    for i in range(1, n+1, 1):
        print(str(i) * i)



# print an n-level pyramid
# Output:
# ____*
# ___***
# __*****
# _*******
# *********

"""
row        spaces        stars
1            4             1
2            3             3
3            2             5 
4            1             7
5            0             9
"""

# r - row number
# n - total number of rows

# the number spaces = n - row number
# the number stars = sum of current and previous row number

def pyramid(n):
    for r in range(1, n+1, 1):
        num_of_spaces = n - r
        num_of_stars = r + (r - 1)
        print(" " * num_of_spaces + "*" * num_of_stars)





"""
print a right arrow
Output:

n = 6

*
**
***  
****
*****
******
*****
****
***
**
*

"""

# n - the number of stars it has to print before it retreats
def right_arrow(n):
    pass

























