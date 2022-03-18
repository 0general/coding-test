"""
https://www.acmicpc.net/problem/6549
"""
import sys

input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    n = arr[0]
    arr = arr[1:]
    arr.append(0)
    mx = 0
    stack = [(0, -1)]
    for i, height in enumerate(arr):
        while stack and stack[-1][0] > height:
            h, idx = stack.pop()
            mx = max(mx, (i-stack[-1][1]-1)*h)
        stack.append((height, i))
    print(mx)
