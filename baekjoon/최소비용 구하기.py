"""
https://www.acmicpc.net/problem/1916
다익스트라
"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
graph = [[-1]*(n+1) for _ in range(n+1)]
distance = [int(1e9)]*(n+1)
for _ in range(int(input())):  # 버스 개수의 범위가 도시의 범위보다 크다. 따라서 가장 적은 비용의 버스만 남긴다.
    f, t, c = map(int, input().split())
    if graph[f][t] == -1:
        graph[f][t] = c
    else:
        graph[f][t] = min(graph[f][t], c)

start, end = map(int, input().split())
h = []
distance[start] = 0
heapq.heappush(h, (0, start))
while h:
    cost, now = heapq.heappop(h)
    if distance[now] < cost:
        continue
    for next, c in enumerate(graph[now]):
        if next == 0 or c == -1:
            continue
        ncost = cost + c
        if ncost < distance[next]:
            distance[next] = ncost
            heapq.heappush(h, (ncost, next))

print(distance[end])
