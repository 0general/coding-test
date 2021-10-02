"""
https://www.acmicpc.net/problem/1747
"""
import sys
from math import *


def palindrome(i):
    test = str(i)
    mid = len(test)//2
    pt2 = len(test)-1
    for pt1 in range(mid):
        if test[pt1] == test[pt2]:
            pt2 -= 1
        else:
            return False
    return True


input = sys.stdin.readline

n = int(input())  # 1~1000000
MAX = 1003001 + 1

# 1000000보다 크고 팰린드롬인 1003001
prime = [i for i in range(MAX)]

for i in range(2, int(sqrt(MAX))+1):
    if prime[i] != 0:
        if i >= n and palindrome(i):
            print(i)
            sys.exit()
        j = 2
        while i*j < MAX:
            prime[i*j] = 0
            j += 1

for i in range(n, MAX):
    if prime[i] != 0 and palindrome(i):
        print(i)
        break
