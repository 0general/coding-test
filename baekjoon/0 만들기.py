"""
https://www.acmicpc.net/problem/7490
"""
import sys

input = sys.stdin.readline


def BT(k, N, num, up, minus, string):
    if k == N:
        num += up*minus
        if num == 0:
            print(string)
        return
    BT(k+1, N, num, up*10+(k+1), minus, string+f" {k+1}")
    BT(k+1, N, num+up*minus, k+1, 1, string+f"+{k+1}")
    BT(k+1, N, num+up*minus, k+1, -1, string+f"-{k+1}")


for _ in range(int(input())):
    N = int(input())
    BT(1, N, 0, 1, 1, "1")
    print()
