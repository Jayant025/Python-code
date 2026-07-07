emp_code = input()

if emp_code.isalnum():
    emp_code = emp_code.upper()
    print(emp_code)

    digits = 0
    for ch in emp_code:
        if ch.isdigit():
            digits += 1

    print("Digits:", digits)
else:
    print("Invalid Employee Code")