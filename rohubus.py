n=4
for row in range(n):
    for space in range(row):
        print(' ',end=' ')
    for col in range(n):
        print('*',end=' ')
    print()