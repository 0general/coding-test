"""
https://www.acmicpc.net/problem/18353
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
for i in range(N):
    if len(stack) == 0 or stack[-1] > arr[i]:
        stack.append(arr[i])
        continue
    s, e = 0, len(stack)-1
    temp = e
    while s <= e:
        mid = (s+e)//2
        if stack[mid] <= arr[i]:
            temp = mid
            e = mid - 1
        else:
            s = mid + 1
    stack[temp] = arr[i]

print(N-len(stack))
