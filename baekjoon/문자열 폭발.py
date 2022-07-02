"""
https://www.acmicpc.net/problem/9935
"""
import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()
n = len(bomb)

stack = []  # 배열이 아닌 string을 쓰면 시간 초과
for s in string:
    stack.append(s)
    if len(stack) >= n and "".join(stack[-n:]) == bomb:
        for _ in range(n):  # pop 이 아닌 slicing을 쓰면 시간 초과
            stack.pop()
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
