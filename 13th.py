member=int(input("check membership\n1.GOLD\n2.SILVER3.REGULAR"))
order=int(input("order price:"))
distance=int(input("delivery distance:"))
pay=int(input("Payment mode:"))
if member==1:
    print("gold membership")
    if order>300:
        print("order accepted")
        if pay==1:
         print("50 rupee cashback")
        else:
         print("no cashback")
    else:
     print("order rejected")
elif member==2:
   print("silver membership")
   if order>500:
      print("order accepted")
      if pay==1:
       print("50 rupee cashback")
      else:
       print("no cashback")
   else:
      print("oreder rejected")
else:
   print("regular membership")
   if order>700:
      print("order accepted")
      if pay==1:
       print("50 rupee cashback")
      else:
       print("no cashback")
   else:
      print("order rejected")
if distance<=5:
   print("free dilivery")
elif distance<=10:
   print("40 rupees charge")
else:
   print("80 rupee charge")
if pay==1:
   print("50 rupee cashback")
else:
   print("no cashback")