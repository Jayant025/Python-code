n = 5

for row in range(n):
    # Print leading spaces
    for space in range(n - row - 1):
        print(" ", end="")

    # Print stars and inner spaces
    for col in range(2 * row + 1):
        if col == 0 or col == 2 * row or row == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()