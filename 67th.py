n=5
for row in range(n):
    for col in range(row+1):
       if row==col:
        print(' ',end='')
       else:
        print('*',end='')
    print()