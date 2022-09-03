"""
https://www.acmicpc.net/problem/16562
"""
import sys
sys.setrecursionlimit(10010)
input = sys.stdin.readline

N, M, k = map(int, input().split())
cost = list(map(int, input().split()))
parent = [i for i in range(N)]


def find_parent(a):
    if parent[a] == a:
        return a
    parent[a] = find_parent(parent[a])
    return parent[a]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if cost[a] <= cost[b]:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union_parent(a, b)

visited = [False for _ in range(N)]

ans = 0
for i in range(N):
    p = find_parent(i)
    if not visited[p]:
        visited[p] = True
        ans += cost[p]
    if ans > k:
        break

if ans > k:
    print("Oh no")
else:
    print(ans)
