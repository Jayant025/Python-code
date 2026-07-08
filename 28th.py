str='''programming'''
nor=""
for ch in str:
 if ch not in nor:
  nor+=ch
 else: 
  nor+='*'
print(nor)