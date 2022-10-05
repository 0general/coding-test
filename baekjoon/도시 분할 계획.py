"""
https://www.acmicpc.net/problem/1647
"""
import sys
import heapq

sys.setrecursionlimit(100010)
input = sys.stdin.readline

N, M = map(int, input().split())
town = N
parent = [i for i in range(N+1)]


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


h = []
answer = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    a, b = min(a, b), max(a, b)
    heapq.heappush(h, (c, a, b))

while town > 2 and h:
    c, a, b = heapq.heappop(h)
    a = find(a)
    b = find(b)
    if a != b:
        union(a, b)
        town -= 1
        answer += c

print(answer)
