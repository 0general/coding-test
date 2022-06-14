"""
https://www.acmicpc.net/problem/1535
"""
import sys

input = sys.stdin.readline

n = int(input())

t = [1 for _ in range(36)]

for i in range(2, 36):
    t[i] = 0
    for j in range(0, i):
        t[i] += t[j]*t[i-j-1]

print(t[n])
