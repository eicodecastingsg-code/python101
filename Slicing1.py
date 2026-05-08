# String Slicing

x = "Roblox-Studio"

print(x[0:6:1])    # Roblox
print(x[7::1])     # it slices up to the last element when stop index is left blank

# when start index is left blank: it starts slicing from the first element
# when stop index is left blank: it slices up to the last element
# when step is left blank, it defaults to 1
print(x[::])

print(x[::-1])     # negative step - slice backward
