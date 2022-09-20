"""
https://www.acmicpc.net/problem/1931
"""
import sys

input = sys.stdin.readline

arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x: (x[1], x[0]))

start = 0
ans = 0

for s, e in arr:
    if s >= start:
        ans += 1
        start = e

print(ans)
