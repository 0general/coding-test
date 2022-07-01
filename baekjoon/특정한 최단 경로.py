"""
https://www.acmicpc.net/problem/1504
"""
from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

MAX = int(1e6)
N, E = map(int, input().split())
arr = [defaultdict(int) for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    arr[b][a] = c

v1, v2 = map(int, input().split())


def dijkstra(s, e):
    dist = [MAX]*(N+1)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        d, now = heapq.heappop(q)
        if d > dist[now]:
            continue
        if now == e:
            break
        for next, cost in arr[now].items():
            nc = d + cost
            if dist[next] > nc:
                dist[next] = nc
                heapq.heappush(q, (nc, next))

    return dist[e]


a, b = dijkstra(1, v1), dijkstra(v2, N)
c, d = dijkstra(1, v2), dijkstra(v1, N)
e = dijkstra(v1, v2)

if e == MAX:
    print(-1)
elif (a < MAX and b < MAX) and (c < MAX and d < MAX):
    print(min(a+b, c+d)+e)
elif (a < MAX and b < MAX):
    print(a+b+e)
elif (c < MAX and d < MAX):
    print(c+d+e)
else:
    print(-1)
