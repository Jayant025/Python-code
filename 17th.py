passw=input("enter password:")
upper=0
lower=0
digit=0
for ch in passw:
 if ch>='A' and ch<='Z':
  upper+=1
 elif ch>='a' and ch<='z':
  lower+=1
 else:
  digit+=1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digit)
if upper>0 and lower>0 and digit>0:
 print("strong password")
else:
 print("week password")
 