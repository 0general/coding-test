"""
https://www.acmicpc.net/problem/11779
"""
import sys
import heapq

input = sys.stdin.readline


INF = int(1e8)+1
L = int(1e5)
n = int(input())
arr = [[L]*(n+1) for _ in range(n+1)]
d = [(INF, 0)]*(n+1)
ans = []

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)

s, e = map(int, input().split())
h = []
d[s] = (0, s)
heapq.heappush(h, (0, s))

while h:
    dist, now = heapq.heappop(h)
    if d[now][0] < dist:
        continue
    for i in range(1, n+1):
        if arr[now][i] == L:
            continue
        nc = dist + arr[now][i]
        if nc < d[i][0]:
            d[i] = (nc, now)
            heapq.heappush(h, (nc, i))

print(d[e][0])
ans.append(e)

while e != s:
    ans.append(d[e][1])
    e = d[e][1]

ans.reverse()
print(len(ans))
print(*ans)
