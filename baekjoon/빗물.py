"""
https://www.acmicpc.net/problem/14719
"""
import sys

input = sys.stdin.readline

H, W = map(int, input().split())
arr = list(map(int, input().split()))

h = max(arr)
idx = 0
now = arr[0]
water = 0
for i in range(W):
    if arr[i] == h:
        idx = i
        break
    if now >= arr[i]:
        water += now-arr[i]
    else:
        now = arr[i]
now = arr[-1]
for i in range(W-1, idx-1, -1):
    if now >= arr[i]:
        water += now-arr[i]
    else:
        now = arr[i]

print(water)
