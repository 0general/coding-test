"""
https://www.acmicpc.net/problem/1978
"""
import sys
import math

input = sys.stdin.readline

n = int(input())
num = [True]*(1001)
num[0], num[1] = False, False

i = 1
for i in range(2, int(math.sqrt(1000))+1):
    if num[i]:
        j = 2
        while i*j <= 1000:
            if num[i*j]:
                num[i*j] = False
            j += 1

check = list(map(int, input().rstrip().split()))
ans = 0
for c in check:
    if num[c]:
        ans += 1

print(ans)
