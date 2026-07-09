s = 'abcda'
uniq = ''

for ch in s:
    if ch in uniq:
       continue
    else:
     uniq += ch

print(uniq)
