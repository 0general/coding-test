"""
https://www.acmicpc.net/problem/17298
"""
import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
stack = []

for i in range(-1, -n-1, -1):
    temp = -1
    while stack:
        if nums[i] >= stack[-1]:
            stack.pop()
        else:
            temp = stack[-1]
            break
    stack.append(nums[i])
    nums[i] = temp

print(*nums)
