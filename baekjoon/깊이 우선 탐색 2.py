"""
https://www.acmicpc.net/problem/24480
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100010)
n, m, r = map(int, input().split())
visited = [0 for _ in range(n+1)]
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

order = 1
visited[r] = order


def dfs(x):
    global order
    arr[x].sort(reverse=True)
    for i in arr[x]:
        if not visited[i]:
            order += 1
            visited[i] = order
            dfs(i)


dfs(r)
for i in range(1, n+1):
    print(visited[i])
