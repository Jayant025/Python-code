parking = int(input("Enter parking hours: "))

if parking <= 2:
    charge = parking * 30

elif parking <= 5:
    charge = (2 * 30) + ((parking - 2) * 50)

else:
    charge = (2 * 30) + (3 * 50) + ((parking - 5) * 80)

print("Parking charge:", charge)