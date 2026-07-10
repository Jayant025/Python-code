wickets = 0
score = 0

while True:
    run = int(input("Enter run (-1 for wide, -2 for wicket): "))
    if run == -1:
        continue
    if run == -2:
        wickets += 1
        if wickets == 10:
            print("All out!")
            break
    else:
        score += run
print("Score =", score)
print("Wickets =", wickets)