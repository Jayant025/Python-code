n=int(input("enter n:"))
sum=0
largest=0
for i in range(1,n):
 if i%2==0:
  if i>largest:
   largest=i
 
print(largest)