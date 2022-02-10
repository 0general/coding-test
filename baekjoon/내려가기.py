"""
https://www.acmicpc.net/problem/2096
"""
import sys

input = sys.stdin.readline

mn = [0, 0, 0]
mx = [0, 0, 0]

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    mn = [arr[0]+min(mn[0], mn[1]), arr[1]+min(mn), arr[2]+min(mn[1], mn[2])]
    mx = [arr[0]+max(mx[0], mx[1]), arr[1]+max(mx), arr[2]+max(mx[1], mx[2])]

print(max(mx), end=' ')
print(min(mn))
