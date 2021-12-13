"""
https://www.acmicpc.net/problem/3020
"""
import sys

input = sys.stdin.readline

N, H = map(int, input().split())
seok = [0]*(H+1)
jong = [0]*(H+1)
n = N//2
for i in range(N):
    h = int(input())
    if i % 2 == 0:  # 석순
        seok[h] += 1
    else:  # 종유석
        jong[h] += 1

for i in range(H-1, 0, -1):
    seok[i] += seok[i+1]
    jong[i] += jong[i+1]

ans = 1
minimum = N

for i in range(1, H+1):
    height = seok[i] + jong[H-i+1]
    if height < minimum:
        ans = 1
        minimum = height
    elif height == minimum:
        ans += 1

print(minimum, ans)
