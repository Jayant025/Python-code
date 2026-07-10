while True:
    fuel = int(input("Enter fuel reading: "))
    if fuel < 0:
        continue
    print("Fuel =", fuel)
    if fuel == 0:
        print("Fuel empty.")
        break