"""
https://www.acmicpc.net/problem/11053
"""
import sys

input = sys.stdin.readline
n = int(input())  # 수열의 크기
nums = list(map(int, input().split()))
dp = [[1, num] for num in nums]  # i번째 수가 선택되었을 때  가장 긴 증가하는 부분 수열
mx = 1  # 수열의 어떤 원소도 반드시 선택된다는 가정이 없으므로 수열 길이의 최대값을 저장할 mx를 따로 지정한다.

for i in range(1, n):
    for j in range(i):
        if nums[i] > dp[j][1]:  # 무조건 자기자신을 마지막으로 두는 경우
            dp[i] = [max(dp[i][0], dp[j][0]+1), nums[i]]
        if dp[i][0] > mx:
            mx = dp[i][0]
            break

print(mx)
