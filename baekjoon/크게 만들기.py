"""
https://www.acmicpc.net/problem/2812
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0
num = input().rstrip()
stack = []
for i in range(n):
    if len(stack) == 0:
        stack.append(num[i])
    else:
        while len(stack) > 0 and stack[-1] < num[i] and k > 0:
            stack.pop()
            k -= 1
        if k == 0:
            stack.append(num[i:])
            answer = int(''.join(stack))
            break
        stack.append(num[i])
else:
    answer = ''.join(stack)
    if k > 0:
        answer = int(answer[:-k])

print(answer)
