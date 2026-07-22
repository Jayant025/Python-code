n=4
for row in range(0,n+1):
    cnt=0
    for col in range(row):
        cnt+=1
        print(cnt,end=' ')
    print()