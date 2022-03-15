"""
https://www.acmicpc.net/problem/1766
"""
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
id = [0]*(N+1)
od = [[] for _ in range(N+1)]
h = []

for _ in range(M):
    a, b = map(int, input().split())
    id[b] += 1
    od[a].append(b)

for i in range(1, N+1):
    if id[i] == 0:
        heapq.heappush(h, i)

while h:
    now = heapq.heappop(h)
    print(now, end=" ")
    for i in od[now]:
        id[i] -= 1
        if id[i] == 0:
            heapq.heappush(h, i)
