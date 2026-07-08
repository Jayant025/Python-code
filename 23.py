str='''aaabbbccdaa'''
nor=""
for i in range(len(str)):
 if i==0 or str[i]!=str[i-1]:
  nor+=str[i]
 else: 
  pass
print(nor)