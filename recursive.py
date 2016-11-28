def recur(t1,t2, n):
	if n == 1:
		return t1
	elif n == 2:
		return t2
	else:
		return recur(t1, t2, n - 2) + recur(t1, t2, n - 1)**2

t1, t2, n = map(int,input().strip().split(' '))
print(recur(t1, t2, n))