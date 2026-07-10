cnt=0
for i in range(1,100):
    rating=int(input("enter rating"))
    if rating>1 and rating<=5:
      continue
    if rating>5:
       print("enter valid rating")
       break
    if rating==1:
       cnt+=1
    if cnt==3:
       print("enough")
       break