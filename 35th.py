#53
n=int(input("enter n:"))
k=int(input("enter k:"))
sum=0
for i in range(1,n+1):
 if i%k!=0:
  sum+=1

print(sum)