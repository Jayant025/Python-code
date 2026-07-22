n=4
cnt=10
for row in range(n,0,-1):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(row):
        print(cnt,end=' ')
        cnt-=1
    print()