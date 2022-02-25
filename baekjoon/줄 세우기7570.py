"""
https://www.acmicpc.net/problem/7570
"""
# 단순하게 가장 긴 증가하는 부분 수열이 아니다.
# 숫자를 옮길 수 있는 방법이 맨 앞 혹은 맨 뒤뿐이기 때문에 중간에 끼울 수 없다.
# 따라서 가장 긴 증가하는 '연속' 부분 수열의 길이를 구하는 것이 관건이다.
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# dp[i] : 숫자 i가 연속된 숫자일때 가장 긴 길이
dp = [0]*(N+1)

for num in arr:
    dp[num] = dp[num-1] + 1

print(N-max(dp))
