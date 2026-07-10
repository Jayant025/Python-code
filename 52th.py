n = int(input("Enter number of students: "))

abs = 0

for i in range(n):
    sta = input().upper()

    if sta != "P" and sta != "A":
        continue

    if sta == "A":
        abs += 1

    if abs == 10:
        print("10 found.")
        break