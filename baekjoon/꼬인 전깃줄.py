"""
https://www.acmicpc.net/problem/1365
"""
import sys

input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

stack = []

for num in arr:
    if len(stack) == 0:
        stack.append(num)
    else:
        if stack[-1] < num:
            stack.append(num)
        if stack[-1] == num:
            continue
        # 이분 탐색 시작
        s, e = 0, len(stack)-1
        ans = e
        while s <= e:
            mid = (s+e)//2
            if stack[mid] >= num:
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        stack[ans] = num

# print(*stack)
print(n-len(stack))
