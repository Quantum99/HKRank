a = input().strip().split(' ')
b = input().strip().split(' ')

pointA,pointB = 0,0

for x in range(3):
	if int(a[x]) > int(b[x]):
		pointA +=1
	if int(b[x]) > int(a[x]):
		pointB += 1

print(pointA,pointB)
