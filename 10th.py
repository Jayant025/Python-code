eli=int(input("enter your marks"))
salary=int(input("enter salary:"))
if(eli>=75):
    if eli>=90:
        print("Merit scholarship")
    elif eli>=80 and eli<=89:
        print("Academic scholarship")
    else:
        print("General scholarship")
    if salary<=200000:
        print("Award full scholarship")
    elif salary>200000 and salary<=500000:
        print("Award 50% scholarship")
    else:
       print("Award 25% scholarship")
else:
    print("you are not eligible for any scholarship")   