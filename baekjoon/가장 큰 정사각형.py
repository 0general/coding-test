"""
https://www.acmicpc.net/problem/1915
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            if i >= 1 and j >= 1:
                arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1
            ans = max(ans, arr[i][j])

print(ans**2)
