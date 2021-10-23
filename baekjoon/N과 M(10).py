"""
https://www.acmicpc.net/problem/15664
"""


def dfs(cnt, idx, string):
    if cnt == m:
        k = len(check)
        check.add(string)
        if k != len(check):
            print(string)
        return
    for i in range(idx+1, n):
        dfs(cnt+1, i, string + " "+str(num[i]))


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
check = set()

for i in range(n):
    dfs(1, i, str(num[i]))
