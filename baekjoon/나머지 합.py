"""
https://www.acmicpc.net/problem/10986
누적합 이용
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num = [0]*m
num[0] = 1
arr = [0] + list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    arr[i] += arr[i-1]
    num[arr[i] % m] += 1

for i in range(m):
    if num[i] < 2:
        continue
    ans += (num[i]*(num[i]-1))//2

print(ans)
