n=4
for row in range(1, n+1):
    for col in range(n-row):
        print(' ', end=' ')
    for st in range(row):
        print('*', end=' ')
    print()

