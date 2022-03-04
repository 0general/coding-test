"""
https://www.acmicpc.net/problem/9466
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)+10)

# O(n)이 되도록 짰다.


def dfs(start, i):
    global n
    if arr[i] == start:  # 시작점과 일치하는 사이클
        n -= visited[i][1]+1
        return
    if not visited[arr[i]]:
        visited[arr[i]] = [start, visited[i][1]+1]
        dfs(start, arr[i])
    else:
        if visited[arr[i]][0] == start:  # 시작점과 일치하지는 않지만 중간에 만나는 사이클
            n -= visited[i][1]-visited[arr[i]][1]+1
            return


for _ in range(int(input())):  # T
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False]*(n+1)
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = [i, 0]
            dfs(i, i)
    print(n)
