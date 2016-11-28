positive = 0
negative = 0
zero = 0

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for a in range(n):
	if arr[a] > 0:
		positive += 1
	elif arr[a] < 0:
		negative += 1
	else:
		zero += 1

print(positive/n)
print(negative/n)
print(zero/n)