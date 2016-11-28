def even_sum(a):
	t1=1
	t2=2
	e_sum = 0
	count = 0
	if a < t2:
		return 0
	else:
		e_sum += t2
		while count < a:
			count = t1 + t2
			t1 = t2	
			t2 = count
			if count % 2 is 0 and count <= a:
				e_sum += t2		
	return e_sum

n = int(input().strip())
arr = []
sums =[]

for s in range(n):
	sums.append(even_sum(int(input().strip())))	

for x in sums:
	print(x)
