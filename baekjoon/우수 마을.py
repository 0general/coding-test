"""
https://www.acmicpc.net/problem/1949
"""
import sys
sys.setrecursionlimit(10010)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ed = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ed[a].append(b)
    ed[b].append(a)

dp = [[arr[i], 0] for i in range(n)]
visited = [False for _ in range(n)]


def dfs(i):
    for e in ed[i]:
        if not visited[e]:  # 자식 노드란 뜻
            visited[e] = True
            temp = dfs(e)
            dp[i][0] += temp[1]  # 내가 우수 마을이므로 자식 노드가 우수 마을이 아닌 경우만
            dp[i][1] += max(temp)
    return dp[i]


visited[0] = True
print(max(dfs(0)))
