s='a1b2c3d15'
letter=""
digit=""
for ch in s:
 if ch>='0' and ch<='9':
  digit+=ch
 else:
  letter+=ch

print(letter+digit)