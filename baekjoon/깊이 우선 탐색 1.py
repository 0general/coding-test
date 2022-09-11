"""
https://www.acmicpc.net/problem/24479
"""
import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
order = 1


def dfs(node):
    global order
    order += 1
    arr[node].sort()
    for x in arr[node]:
        if not visited[x]:
            visited[x] = order
            dfs(x)


for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited[R] = order
dfs(R)

for i in range(1, N+1):
    print(visited[i])
