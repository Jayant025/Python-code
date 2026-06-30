product=int(input("enter prices:"))
customer=int(input("cus. type1/2:"))
if customer==1:
  print("regular customers")
  if product>5000:
    bill = product - product * .1
    print(bill)
  else:
   bill = product
   print(bill)

elif customer==2:
  print("Premium customers!")
  bill = product-product*.2
  print(bill)
else:
 print("invalid")
 