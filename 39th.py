pro_code=input("enter your P. id")

if len(pro_code)==6:
 if pro_code[0:3].isupper() and pro_code[0:3].isalpha():
   if pro_code[2:].isdigit():
     total=0
     for ch in pro_code:
      total+=int(ch)

      
     if total > 15:
        print("Valid Product Code")
     else:
        print("Invalid Product Code")
   else:
     print("Invalid Product Code")
 else:
    print("Invalid Product Code")
else:
    print("Invalid Product Code")