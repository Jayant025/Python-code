text = "I am a student of skit college"
print(text.swapcase())
cnt=0
for ch in text:
	if ch.lower() in 'aeiou':
		cnt+=1
		
print("vowels:",cnt)
 