n=4
for row in range(n):
    for col in range(row*3):
        print(' ', end='')
    for star in range(n-row):
        print('*', end='  ')
    print()
