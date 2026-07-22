n=4
cnt=1
for row in range(n,0,-1):
    for space in range(n-row):
        print(' ',end=' ')
    for col in range(row):
        print(cnt,end=' ')
        cnt+=2
    print()

    #if row loop sidha chalta to mujhe space row se
    # start karna tha or col n-row se vise versa hota
