text = "DataScienceWithPython"
print(text[11:])
print(text[1:-1])
print(text[1:-2])
print(text[::-2])
username = input("Enter username: ")

if username.isalpha():
    print(username.lower())
else:
    print("Invalid Username")