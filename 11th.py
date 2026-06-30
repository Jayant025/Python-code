pas = int(input("Passport Available(1/0):"))
visa=int(input("Visa available(1/0):"))
bag=int(input("Bag weight:"))
hr=int(input("time of arrival before flight:"))
if pas==1:
    print("have passport")
    if visa==1:
     print("visa is valid")
     if bag<=20:
      print("no extra charge")
     elif bag<=30:
      print("give 1500 extra charge")
     else:
      print("Baggage not allowed")
     if hr>=2:
      print("boarding pass generated")
     else:
      print("Late Arrival\nBoarding Cancelled")
    else:
     print("Boarding Denied\nReason : Invalid Visa")
else:
 print("Boarding Denied\nReason : Passport Missing")
 