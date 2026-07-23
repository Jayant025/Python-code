n=5
cnt=1
for row in range(n):
    for space in range(n-row-1):
        print(' ',end=' ')
    for star in range(row):
        print(row,end=' ')
    print()