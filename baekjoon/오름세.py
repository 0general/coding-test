"""
https://www.acmicpc.net/problem/3745
"""
import sys

input = sys.stdin.readline

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        stack = []
        for num in arr:
            if len(stack) == 0:
                stack.append(num)
                continue
            if stack[-1] < num:
                stack.append(num)
            else:
                s, e = 0, len(stack)-1
                ans = 0
                while s <= e:
                    mid = (s+e)//2
                    if stack[mid] >= num:
                        ans = mid
                        e = mid - 1
                    else:
                        s = mid + 1
                stack[ans] = num
        print(len(stack))
    except:
        break
