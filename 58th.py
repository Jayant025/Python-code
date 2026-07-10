sum=0
for i in range(0,100):
    n=int(input())
    if i<0:
     continue
    else:
     sum+=n
     if sum>1000:
       print("exceed limit!!!")
       break