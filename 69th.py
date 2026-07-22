n=5
for row in range(n):
    for col in range(n):
      if row==(n-1)//2 or col==(n-1)//2:
         print("*",end=' ')
      else:
         print(" ",end=' ')
    print()