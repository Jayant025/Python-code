n=4
cnt=2
for row in range(0,n+1):
    for col in range(row):
        print(cnt,end=' ')
        cnt+=2
    print()