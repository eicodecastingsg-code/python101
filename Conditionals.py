"""
Variations of conditionals:
1. if
2. if - elif(s)
3. if - elif(s) - else
4. if - else
"""

# Type 1 conditional
if 10 > 2:
    print("^_^")



# Type 2 conditional
# It executes ONLY the FIRST TRUE statement
if 10 > 100:
    print("A")
elif 10 > 200:
    print("B")
elif 10 > 3:
    print("C")
elif 10 > 400:
    print("D")


# Type 2 conditional
x = 50
if x > 100:
    print("E")
elif x > 10:
    print("F")
elif x > 20:
    print("G")
elif x > 30:
    print("H")


# Type 2 conditonal
y = "ROBLOX"
if len(y) == 10:
    print("I")
elif len(y) == 11:
    print("J")
elif len(y) == 12:
    print("K")


# Type 3 conditional
# the else clause guarantees an output
z = 5
if z % 2 == 0:
    print("L")
elif z + 2 == 10:
    print("M")
else:
    print("N")















