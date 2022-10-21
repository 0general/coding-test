"""
https://www.acmicpc.net/problem/1009
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = 1
    while b != 0:
        if b & 1:
            ans = (ans * a) % 10
        a = (a*a) % 10
        b >>= 1
    if ans:
        print(ans)
    else:
        print(10)
