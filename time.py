time = input().strip().split(':')
hour = int(time[0])
minute = time[1]
st = str(time[2])
seconds = st[0:2]
dat = st[2:]

if dat == "PM" and hour != 12:
	print(str(hour + 12) + ':' + minute + ':' + seconds)
elif dat == "AM" and hour == 12:
	h = "00"
	print(h + ":" + minute + ":" + seconds)
elif dat == "AM" and hour < 10:
	h = "0" + str(hour)
	print(h + ":" + minute + ":" + seconds)
else:
	print(str(hour) + ':' + minute + ':' + seconds)
