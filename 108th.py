n=4
for row in range(1,n+1):
    for space in range(n-row):
       print(' ',end=' ')
    for col in range(row):
     print('*',end=' ')
    print()