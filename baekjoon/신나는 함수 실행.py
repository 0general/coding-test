"""
https://www.acmicpc.net/problem/9184
"""
import sys

input = sys.stdin.readline
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                dp[i][j][k] = 1
            elif i < j and j < k:
                b = j-1 if j > 0 else 0
                c = k-1 if k > 0 else 0
                dp[i][j][k] = dp[i][j][c] + dp[i][b][c] - dp[i][b][k]
            else:
                a = i-1 if i > 0 else 0
                b = j-1 if j > 0 else 0
                c = k-1 if k > 0 else 0
                dp[i][j][k] = dp[a][j][k] + \
                    dp[a][b][k] + dp[a][j][c] - dp[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        print(f"w({a}, {b}, {c}) = {dp[0][0][0]}")
    elif a > 20 or b > 20 or c > 20:
        print(f"w({a}, {b}, {c}) = {dp[20][20][20]}")
    else:
        print(f"w({a}, {b}, {c}) = {dp[a][b][c]}")
