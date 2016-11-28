import sys


n = int(input().strip())
a = []
s1 = 0
s2 = 0
i = 1

for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    s1 += a_t[a_i]
    s2 += a_t[n - i]
    i += 1

print(abs(s2 - s1))
