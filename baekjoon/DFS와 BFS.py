'''
https://www.acmicpc.net/problem/1260
'''
from collections import deque


def dfs(adj, v, visited):
    visited[v] = True
    print(v, end=' ')
    if v in adj:
        for i in adj[v]:
            if not visited[i]:
                dfs(adj, i, visited)


def bfs(adj, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        nv = queue.popleft()
        print(nv, end=' ')
        if nv in adj:
            for i in adj[nv]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


# 정점 수, 간선 개수, 시작 정점
n, m, v = list(map(int, input().split()))
visited1 = [False]*(n+1)
visited2 = [False]*(n+1)
adj = dict()
for _ in range(m):
    i, j = map(int, input().split())
    if i in adj:
        adj[i].append(j)
    else:
        adj[i] = [j]
    if j in adj:
        adj[j].append(i)
    else:
        adj[j] = [i]
    adj[i].sort()
    adj[j].sort()


dfs(adj, v, visited1)
print()
bfs(adj, v, visited2)
