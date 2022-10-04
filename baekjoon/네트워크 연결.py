"""
https://www.acmicpc.net/problem/1922
"""
import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
road = [[10001 for _ in range(N+1)] for _ in range(N+1)]
h = []
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    a, b = min(a, b), max(a, b)
    if road[a][b] < c:
        continue
    heapq.heappush(h, (c, a, b))


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


cost = 0
while h:
    c, a, b = heapq.heappop(h)
    a = find(a)
    b = find(b)
    if a != b:
        cost += c
        union(a, b)

print(cost)
