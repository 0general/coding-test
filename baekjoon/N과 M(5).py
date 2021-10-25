"""
https://www.acmicpc.net/problem/15654
"""


def BT(cnt, i, string):
    if cnt == m:
        print(string)
        return
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            BT(cnt+1, j, string + " " + str(num[j]))
            visited[j] = False


n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = [False]*n

for i in range(n):
    visited[i] = True
    BT(1, i, str(num[i]))
    visited[i] = False
