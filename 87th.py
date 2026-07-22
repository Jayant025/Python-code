n=4
for row in range(0,n):
    cnt=0
    for col in range(n-row):
        cnt+=1
        print(cnt,end=' ')
    print()