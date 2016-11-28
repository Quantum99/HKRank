n,m = map(int,input().split())

if n > m:
	print(n - m)
elif n is m:
	print(n//m)
else:
	print(abs(m//n))