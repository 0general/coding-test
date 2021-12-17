"""
https://www.acmicpc.net/problem/5972
다익스트라
"""
import sys
import heapq

input = sys.stdin.readline

INF = int(1e7)*5+1
N, M = map(int, input().split())
graph = [{} for _ in range(N)]
distance = [INF]*N

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = min(graph[a].get(b, 1001), graph[b].get(a, 1001), c)
    graph[b][a] = graph[a][b]

h = []
distance[0] = 0
heapq.heappush(h, (0, 0))

while h:
    cow, now = heapq.heappop(h)
    if distance[now] < cow:
        continue
    for next in graph[now]:
        cost = graph[now][next] + cow
        if cost < distance[next]:
            distance[next] = cost
            heapq.heappush(h, (cost, next))

print(distance[N-1])
