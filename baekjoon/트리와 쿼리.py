"""
https://www.acmicpc.net/problem/15681
"""
import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
edges = [[] for _ in range(N+1)]
size = [0 for _ in range(N+1)]


def tree_dfs(root):
    size[root] = 1
    for v in edges[root]:
        if size[v] == 0:
            size[root] += tree_dfs(v)
    return size[root]


for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

tree_dfs(R)

for _ in range(Q):
    print(size[int(input())])
