'''
https://www.acmicpc.net/problem/12101
'''
import sys
input = sys.stdin.readline

t = int(input())
num = []
for _ in range(t):
    num.append(int(input()))
dp = [1] * (max(num)+1)
dp[1], dp[2] = 1, 2
for i in range(3, len(dp)):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009
    # 수 (i-3)에서 3 더하는 경우, (i-2)에서 2 더하는 경우, (i-1)에서 1 더하는 경우

for i in num:
    print(dp[i])  # 여기서 %1000000009 를 하게 되면 메모리 초과가 난다.
