passs='@Jayant2004'
cnt=5
for i in range(7):
    pas_wr=input("enter your passwr:")
    if pas_wr!=passs:
        cnt-=1
        print("wrong password")
    if cnt<=0:
        print("accout locked")
        break

