from math import sqrt
from math import ceil

m, n = map(int, input().split())

che = list(range(n+1))

for i in range(2, ceil(sqrt(n))+1):
    s = 2
    while i*s <= n:
        che[i*s] = 0
        s += 1

for i in che[m:]:
    if i > 1:
        print(i)
