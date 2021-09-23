"""
https://www.acmicpc.net/problem/15651

1부터 N까지 M번을 고른 모든 수열
중복 선택 가능
"""


def BT(s, num):
    if num == m:
        print(s)
    else:
        for i in range(n):
            BT(s+" "+su[i], num+1)


n, m = map(int, input().split())
su = [str(i) for i in range(1, n+1)]

for i in range(n):
    s = ""
    BT(s+su[i], 1)
