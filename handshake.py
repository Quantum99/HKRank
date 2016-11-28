def handshake(n):
	return int(n * ((n-1) / 2))

n = []
T = int(input().strip())
for a0 in range(T):
    n.append(int(input().strip()))
    
for x in range(T):
	print(int((n[x] * n[x] - n[x]) / 2))