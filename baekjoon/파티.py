"""
https://www.acmicpc.net/problem/1238
다익스트라
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e6)+1


def dijkstra(s, e):
    h = []
    distance = [INF]*(N+1)
    heapq.heappush(h, (0, s))
    while h:
        time, now = heapq.heappop(h)
        if distance[now] < time:
            continue
        for n, t in graph[now]:
            cost = time + t
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(h, (cost, n))

    return distance[e]


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

mx = 0
for s in range(1, N+1):
    if s == X:
        continue  # X->X인 경로 있을 수 있음.
    mx = max(dijkstra(s, X) + dijkstra(X, s), mx)

print(mx)
