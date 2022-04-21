"""
https://www.acmicpc.net/problem/1083
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

s = int(input())

for i in range(n):
    if s == 0:
        break
    mx = arr[i]
    idx = i
    for j in range(i+1, min(i+1+s, n)):
        if arr[j] > mx:
            mx = arr[j]
            idx = j
    if idx == i:
        continue
    for k in range(idx, i, -1):
        arr[k] = arr[k-1]
    arr[i] = mx
    s -= idx-i

print(*arr)
