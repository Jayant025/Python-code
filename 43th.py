sum=0
for i in range(0,10):
 sales=int(input("enter your sale:"))
 sum+=sales
 if sum>=100000:
  print("total sale exceed 100000!!")
  break
