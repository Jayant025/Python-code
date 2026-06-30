asa=int(input("Enter salary"))
print(asa)
if asa<=400000:
    tax=asa*0.0
    print(tax)
elif asa>400000 and asa<=800000:
    tax=asa*0.1
    print(tax)
elif asa>800000 and asa<=1200000:
    tax=asa*0.2
    print(tax)
else:
    tax=asa*.3
    print(tax)

