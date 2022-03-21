"""
https://www.acmicpc.net/problem/1644
"""
import sys
from math import sqrt

input = sys.stdin.readline
n = int(input())

pnum = [True]*(n+1)
pnum[0], pnum[1] = False, False

# 소수 구하기 - 에라토스테네스의 체
for num in range(2, int(sqrt(n))+1):
    if num:
        i = 2
        while num*i <= n:
            pnum[num*i] = False
            i += 1

arr = [0] + [i for i in range(len(pnum)) if pnum[i]]

# 누적합 이용
for i in range(1, len(arr)):
    arr[i] += arr[i-1]

ans = 0

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        num = arr[j]-arr[i]
        if num == n:
            ans += 1
        elif num > n:  # 숫자가 더 크지면 안됨
            break

print(ans)
