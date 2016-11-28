n = int(input())
count = []
for _ in range(n):
	dels = 0
	word = str(input().split())
	for i in range(0,len(word)-1):
		if word[i] == word[i +1]:
			dels += 1 
	count.append(dels)

for y in count:
	print(y)