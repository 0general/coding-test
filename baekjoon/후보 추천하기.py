"""
https://www.acmicpc.net/problem/1713
"""
import math
import sys

input = sys.stdin.readline
# year = Ma+x = Nb+y 인 year 찾기

# 연립 일차 합동식 공부해서 다시 해볼 것.
T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    last = (m*n)//math.gcd(m, n)  # LCM 최소공배수이자 마지막 해
    if m == x and n == y:
        print(last)
        continue
    i = 0
    num = 0
    ans = -1
    while num < last:
        num = m*i + x
        if num % n == y % n:
            ans = num
            break
        i += 1
    print(ans)
