n=4
for row in range(n,0,-1):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(row):
        print(row,end=' ')
    print()