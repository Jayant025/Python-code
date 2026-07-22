n=4
cnt=0
for row in range(0,n+1):
    for col in range(row):
        cnt+=1
        print(cnt,end=' ')
    print()