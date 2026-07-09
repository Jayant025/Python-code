n=int(input("enter number"))
k=int(input("enter number k:"))
 
for i in range(0,n+k+1):
    if i%k==0:
        if i>=n:
         print(i)
         break