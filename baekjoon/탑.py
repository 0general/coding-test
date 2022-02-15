"""
https://www.acmicpc.net/problem/2493
"""
import sys

input = sys.stdin.readline


n = int(input())
top = list(map(int, input().split()))
stack = []
ans = []

idx = 1
for h in top:
    while stack:
        if stack[-1][0] >= h:
            break
        else:
            stack.pop()
    if len(stack) == 0:
        ans.append(0)
        stack.append((h, idx))
    else:
        ans.append(stack[-1][1])
        stack.append((h, idx))
    idx += 1

print(*ans)
