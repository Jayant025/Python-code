idc = 'CS205'
idi = 'IT206'

if idc[0:2].isupper() and idc[0:2] == 'CS':
    if idc[2:].isdigit() and len(idc[2:]) == 3 and 101 <= int(idc[2:]) <= 300:
        print("Valid Registration Number")
    else:
        print("Invalid Registration Number")
else:
    print("Invalid Registration Number")


if idi[0:2].isupper() and idi[0:2] == 'IT':
    if idi[2:].isdigit() and len(idi[2:]) == 3 and 101 <= int(idi[2:]) <= 300:
        print("Valid Registration Number")
    else:
        print("Invalid Registration Number")
else:
    print("Invalid Registration Number")