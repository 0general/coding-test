"""
https://www.acmicpc.net/problem/9012
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    num = 0  # 스택 역할
    for s in input().rstrip():
        if s == '(':
            num += 1
        else:
            num -= 1
            if num < 0:  # stack이 비어있을 때 pop을 시도한 경우
                break
    if num == 0:
        print("YES")
    else:
        print("NO")
