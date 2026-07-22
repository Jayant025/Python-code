n=4
for row in range(n):
    for space in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print(n-row,end=' ')
    print()