"""
https://www.acmicpc.net/problem/15652
"""


def BT(cnt, num, string):
    if cnt + 1 == m:
        print(string)
        return
    for i in range(num, n+1):
        BT(cnt+1, i, string+" "+str(i))


n, m = map(int, input().split())

for i in range(1, n+1):
    BT(0, i, str(i))
