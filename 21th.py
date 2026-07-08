str='''jayant'''
pal=str
rev=""
for ch in range(len(str)-1,-1,-1):
  rev+=str[ch]

if rev==str:
 print("it is pal")
else:
  print("it is not pal")