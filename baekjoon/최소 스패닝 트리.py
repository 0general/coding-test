"""
https://www.acmicpc.net/problem/1197
"""
import sys

input = sys.stdin.readline
v, e = map(int, input().split())
parent = [i for i in range(v+1)]
h = []
for _ in range(e):
    a, b, c = map(int, input().split())
    a, b = min(a, b), max(a, b)
    h.append((c, a, b))

h.sort(key=lambda x: x[0])


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0

for edge in h:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost

print(answer)
