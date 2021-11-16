"""
https://www.acmicpc.net/problem/2352
"""
import sys


def BS(num):
    if len(stack) == 0:
        stack.append(num)
        return
    if stack[-1] < num:
        stack.append(num)
        return
    s, e = 0, len(stack)-1
    ans = 0
    while s <= e:
        mid = (s + e)//2
        if stack[mid] < num:
            s = mid + 1
        else:
            ans = mid
            e = mid - 1

    stack[ans] = num
    return


input = sys.stdin.readline
n = int(input())
stack = []
nums = list(map(int, input().rstrip().split()))

for num in nums:
    BS(num)

print(len(stack))
