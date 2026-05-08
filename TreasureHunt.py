import random

print("\n 🏴‍ ☠️ Welcome to the Pirate Island 🏴‍ ☠️")
size = int(input("Enter map size (e.g., 5 for a 5 x 5 map): "))
print(f"Guess the treasure location on a {size} x {size} map.")

# create a treasure map with a 2D List using list comprehension
map = [ ["?" for j in range(size)] for i in range(size) ]

# plant a treasure at a random spot on the map
treasure_row = random.randint(0, size - 1)
treasure_col = random.randint(0, size - 1)

attempts = 0


def show_map(map):
    # for each row, print all columns
    for row in map:
        for col in row:  # print 1 row
            print(col, end=" ")
        print()  # go to the next line


show_map(map)


while True:

    try:
        # collect row and col inputs
        row = int(input(f"Enter row number (0 - {size - 1}): "))
        col = int(input(f"Enter col number (0 - {size - 1}): "))
    except ValueError:
        print("⚠️ Please enter numbers only")
        continue  # skip all codes below and quickly begin the next repetition


    # check if row and col numbers are within range
    if not(0 <= row < size and 0 <= col < size):
        continue

    attempts = attempts + 1

    # check guess
    if row == treasure_row and col == treasure_col:
        print("HOORAY! You found the treasure!")
        map[row][col] = "⭐"
        show_map(map)
        print(f"Attempts: {attempts}")
        break

    else:
        print("❌ Wrong spot. Did you even try?")
        map[row][col] = "X"
        show_map(map)

        # give hint
        if col > treasure_col:
            print("The treasure is further LEFT")

        if col < treasure_col:
            print("The treasure is further RIGHT")

        if row > treasure_row:
            print("The treasure is further UP")

        if row < treasure_row:
            print("The treasure is further DOWN")













