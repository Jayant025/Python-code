n=6
for row in range(n):
    for space in range(n-row-1):
        print(" ",end="")
    for star in range(row+1):
          print('*',end=' ')
    print()         