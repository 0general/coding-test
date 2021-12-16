"""
https://www.acmicpc.net/problem/1753
"""
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
graph = [{} for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = min(graph[u].get(v, 2000001), w)

distance = [200001]*(V)
distance[k-1] = 0
h = [(0, k-1)]
heapq.heapify(h)

while h:
    dist, now = heapq.heappop(h)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + graph[now][i]
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(h, (cost, i))

for i in range(V):
    if distance[i] == 200001:
        print("INF")
    else:
        print(distance[i])
