salary=int(input("Enter salary:"))
employ=int(input("enter your type:\n1.goverment job\n2.private job\n3.self employed"))
credit=int(input("enter your score"))
loans=int(input("total number of loans you have now:"))
if salary>40000:
    print("salary verified")
    if employ==1:
       print("Goverment job")
       if credit>=700:
          print("okk")
          if loans>2:
             print("Loan rejected")
          else:
             print("loan approved")
       else:
          print("not meet to requirement")
    elif employ==2:
       print("Private job")
       if credit>=750:
          print("okk")
          if loans>2:
             print("Loan rejected")
          else:
             print("loan approved")
       else:
          print("not meet to requirement")
    else:
       print("self employed")
       if credit>=780:
          print("okk")
          if loans>2:
             print("Loan rejected")
          else:
             print("loan approved")
       else:
          print("not meet to requirement")
    
else:
 print("Loan Rejected\nSalary Requirement Not Met")
