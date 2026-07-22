n=4
cnt=0
for row in range(n,0,-1):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(row):
        cnt+=1
        print(cnt,end=' ')
    print()