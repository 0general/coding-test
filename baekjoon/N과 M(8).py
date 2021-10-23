"""
https://www.acmicpc.net/problem/15657
"""


def dfs(cnt, idx, string):
    if cnt == m:
        print(string)
        return
    for i in range(idx, n):
        if cnt == 0:
            dfs(cnt+1, i, str(num[i]))
        else:
            dfs(cnt+1, i, string + " " + str(num[i]))


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

dfs(0, 0, "")
