t = int(input())
win = []
for ca in range(t):
	g = int(input())
	for co in range(g):
		piles = int(input())
		stones = [int(x) for x in input("").split(" ")]
		turns[co] = sum([(a-1)/2 for a in stones[co]])
	
	turn_num = sum(nTurns)	

	if(turn_num % 2):
		print("Alice")
	else:
		print("Bob")
	