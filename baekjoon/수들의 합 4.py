"""
https://www.acmicpc.net/problem/2015
"""
from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
num = defaultdict(int)
num[0] = 1
ans = 0
for i in range(N):
    if i != 0:
        arr[i] += arr[i-1]
    ans += num[arr[i]-K]
    num[arr[i]] += 1  # i번째까지의 누적합

print(ans)
