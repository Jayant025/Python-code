n=4
for row in range(n):
    for col in range(row+1):
        if row==3 or col == 0 or row == col:
         print('*',end="")
        else:
           print(' ',end="")
    print()