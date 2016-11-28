def get_draws(a):
	return a+1

t = int(input().strip())
draws = []

for x in range(0,t):
	draws.append(get_draws(int(input().strip())))

for x in range(0,t):
	print(draws[x])