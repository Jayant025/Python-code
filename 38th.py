passwor=input("enter your password")
has_upper=False
has_lower=False
has_digit=False
for ch in passwor:
  if ch.isupper():
   has_upper=True

  if ch.islower():
   has_lower=True

  if ch.isdigit():
   has_digit=True

if len(passwor) >= 8 and has_upper and has_lower and has_digit:
  print("strong password")
else:
 print("weak password")

