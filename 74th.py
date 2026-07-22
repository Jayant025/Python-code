n=6
for row in range(n):
    for col in range(n-row):
      if col==0 or row==0 or col==n-row-1:
        print("*",end=" ")
      else:
         print(' ',end=' ')
    print()     