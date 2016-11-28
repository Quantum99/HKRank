def changes(colours):
	reps = []
	count = 0
	for item in colours:
		if colours.count(item) > 1:
			reps.append(item)
	for s in range(len(colours)):
		brush1 = colours[s]
		if brush1 in reps:
			brush2 = colours[s + 1]
			count += 1
			if brush2 in reps:
				brush2 = colours[s + 1]
			else:
				brush1 = colours[s + 1]

	return brush1
t = int(input())
change = []
for x in range(t):
	n = int(input())
	c = input().strip().split()
	change.append(changes(c))

for c in change:
	print(c)
print(change)