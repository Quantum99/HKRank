import sys

pairs = 0
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

for x in range(0,len(a)):
	for v in range(x+1,len(a)):
		if (a[x] + a[v]) % k == 0:
			pairs += 1

print(pairs)
