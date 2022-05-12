"""
https://www.acmicpc.net/problem/1806
"""
import sys

input = sys.stdin.readline

ans = 100001

N, S = map(int, input().split())

arr = [0] + list(map(int, input().split()))

l = 0
for r in range(1, N+1):
    arr[r] += arr[r-1]
    while l < r:
        x = arr[r] - arr[l]
        if x < S:
            break
        ans = min(ans, r-l)
        l += 1

if ans == 100001:
    print(0)
else:
    print(ans)
