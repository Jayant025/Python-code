accbal=int(input("enter balance"))
withamt=int(input("withdrawal amt:"))
print(accbal)
print(withamt)
if withamt%100==0:
    if accbal-withamt<1000:
        print("invalid balance")
    else:
     accbal=accbal-withamt
     print("withdrawal successful!")
     print(accbal)
else:
 print("Withdrawal amount must be multiple of 100")