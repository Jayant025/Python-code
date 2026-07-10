n=int(input())
for i in range(0,n+13+1):
 if i%4==0:
  continue
 if i%13==0:
   break
 else:
  print(i)