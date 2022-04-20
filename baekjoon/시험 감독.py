"""
https://www.acmicpc.net/problem/13458
"""
import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
b, c = map(int, input().split())

answer = n
for i in range(n):
    A[i] -= b
    if A[i] > 0:
        answer += A[i]//c
        if A[i] % c != 0:
            answer += 1

print(answer)
