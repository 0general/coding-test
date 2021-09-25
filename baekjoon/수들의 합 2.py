"""
https://www.acmicpc.net/problem/2003
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [0] + list(map(int, input().split()))

for i in range(2, n+1):
    num[i] += num[i-1]

cnt = 0
for i in range(1, n+1):
    for j in range(i):
        if num[i] - num[j] == m:
            cnt += 1
print(cnt)
