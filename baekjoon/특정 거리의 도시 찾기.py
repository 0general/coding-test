"""
https://www.acmicpc.net/problem/18352
"""
import heapq
import sys

input = sys.stdin.readline
INF = 300001
N, M, K, X = map(int, input().split())
dist = [INF]*(N+1)
arr = [set() for _ in range(N+1)]
dist[X] = 0
h = []
ans = set()
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].add(b)

heapq.heappush(h, (0, X))
while h:
    c, n = heapq.heappop(h)
    if dist[n] < c:
        continue
    if c >= K:
        continue
    for i in arr[n]:
        t = c+1
        if t < dist[i]:
            dist[i] = t
            if t == K:
                ans.add(i)
            else:
                heapq.heappush(h, (t, i))


if len(ans) == 0:
    print(-1)
else:
    for i in sorted(list(ans)):
        print(i)
