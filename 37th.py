emp_id='ABCa1234'
start=emp_id[0:3]
print(start)
digit=True
end=emp_id[-3:]
upper=False
for i in range(len(start)):
 if not end[i].isdigit():
  digit=False
 if not start[i].isupper():
  upper=False
 if digit and upper:
  print("valid employee id")
 else: 
  print("Invalid")
 