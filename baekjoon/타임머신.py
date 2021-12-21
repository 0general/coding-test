"""
https://www.acmicpc.net/problem/11657
벨만 포드 (음의 가중치 처리 가능)
"""
import sys


INF = int(1e7)
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
distance = [INF]*(n+1)
for _ in range(m):
    edges.append(tuple(map(int, input().split())))

distance[1] = 0
for i in range(1, n):  # V-1회 시작 노드를 제외한 모든 노드의 수만큼 edge relaxation(최단 경로를 구성하는 node와 edge에 대한 정보, 그리고 거리의 합을 업데이트)
    for edge in edges:
        now, next, cost = edge
        dist = distance[now] + cost
        if distance[now] != INF and dist < distance[next]:
            distance[next] = dist

for edge in edges:  # 만약 거리 정보가 바뀐다면 음의 사이클이 발생했다는 의미
    now, next, cost = edge
    dist = distance[now] + cost
    if distance[now] != INF and dist < distance[next]:
        print(-1)
        break
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
