total = 0
while True:
    toll = int(input("Enter toll amount: "))
    if toll == 0:
        continue
    total += toll

    if total > 50000:
        print("Collection stopped.")
        break
print("Total Collection =", total)