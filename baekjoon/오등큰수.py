"""
https://www.acmicpc.net/problem/17299
"""
import sys

input = sys.stdin.readline

N = int(input())
num = [0]*(int(1e6)+1)
arr = list(map(int, input().split()))
ans = [-1]*N

stack = []
for a in arr:
    num[a] += 1

for i in range(N-1, -1, -1):
    while stack:
        if num[stack[-1]] <= num[arr[i]]:
            stack.pop()
        else:
            break
    if stack:
        ans[i] = stack[-1]
    stack.append(arr[i])

print(*ans)
