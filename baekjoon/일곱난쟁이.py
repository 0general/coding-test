"""
https://www.acmicpc.net/problem/2309
"""

h = []
for _ in range(9):
    h.append(int(input()))

h.sort()
hap = sum(h)
x, y = -1, -1
for i in range(9):
    for j in range(i+1, 9):
        n = h[i]+h[j]
        if hap - n == 100:
            x, y = i, j
            break
    if x != -1 and y != -1:
        break

for i in range(9):
    if i != x and i != y:
        print(h[i])
