'''
https://www.acmicpc.net/problem/11724
'''
import sys
input = sys.stdin.readline


def dfs(i):
    for j in arr[i]:
        if not visit[j]:
            visit[j] = True
            dfs(j)
    return


cnt = 0
n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, n+1):
    if not visit[i]:
        visit[i] = True
        dfs(i)
        cnt += 1

print(cnt)
