"""
https://www.acmicpc.net/problem/16197
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

ans = -1
visited = set()
x = []
arr = []
for i in range(n):
    arr.append(list(input().rstrip()))
    for j in range(m):
        if arr[i][j] == 'o':
            x.append((i, j))

visited.add(tuple(x))
q = deque()
q.append((x, 0))

dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]

while q:
    temp, num = q.popleft()
    if num >= 10:
        break
    for d in dir:
        ok = 0
        x1, y1 = temp[0][0]+d[0], temp[0][1]+d[1]
        x2, y2 = temp[1][0]+d[0], temp[1][1]+d[1]
        if x1 < 0 or y1 < 0 or x1 >= n or y1 >= m:
            ok += 1
        if x2 < 0 or y2 < 0 or x2 >= n or y2 >= m:
            ok += 1
        if ok == 1:
            ans = num + 1
            break
        if ok:
            continue
        if arr[x1][y1] == '#':
            x1, y1 = temp[0]
        if arr[x2][y2] == '#':
            x2, y2 = temp[1]
        nx = ((x1, y1), (x2, y2))
        if nx not in visited:
            visited.add(nx)
            q.append((nx, num+1))
    else:
        continue
    break


print(ans)
