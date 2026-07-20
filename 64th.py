n=int(input())
i=0
while(i<=500):
 if i%4==0 and i%6==0:
  if i>n:
   print(i)
   break
 i+=1