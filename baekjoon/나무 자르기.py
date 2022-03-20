"""
https://www.acmicpc.net/problem/14247
"""
import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += a[i] + (n-1)*d[i]

d.sort(reverse=True)

for i in range(n):
    ans -= i*d[i]

print(ans)
