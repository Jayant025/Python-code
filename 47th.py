k=17
n=200
for i in range(n+k+1):
    if i % k==0:
     if i>n:
        print(i)
        break
     else:
        continue