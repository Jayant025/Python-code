balance=10000
cnt=0
for i in range(0,30):
    daily_exp=int(input("enter daily expense:"))
    balance=balance-daily_exp
    if balance<0:
     print("insufficient balance\n","day on which negative:",cnt)
     break
    else:
       cnt+=1