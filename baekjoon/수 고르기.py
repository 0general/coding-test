"""
https://www.acmicpc.net/problem/2230
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()
ans = arr[-1]-arr[0]

s, e = 0, 0
while e < n:
    if s >= e:
        e += 1
        continue
    x = arr[e]-arr[s]
    if x >= m:
        ans = min(ans, x)
        s += 1
    else:
        e += 1

print(ans)
