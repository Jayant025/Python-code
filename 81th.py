n=4
for row in range(n,0,-1):
    for col in range(n-row+1):
        print(row,end=' ')
    print()