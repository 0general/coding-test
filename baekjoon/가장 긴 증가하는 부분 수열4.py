"""
https://www.acmicpc.net/problem/14002
"""
import sys

input = sys.stdin.readline
n = int(input())  # 수열의 크기
nums = list(map(int, input().split()))
# i번째 수가 선택되었을 때  가장 긴 증가하는 부분 수열의 길이, 수열의 i-1번째 수의 인덱스
dp = [[1, -1] for num in nums]
mx = 1  # 수열의 어떤 원소도 반드시 선택된다는 가정이 없으므로 수열 길이의 최대값을 저장할 mx를 따로 지정한다.
last = 0  # mx를 가지고 있는 위치의 인덱스. 즉, 가장 긴 증가하는 부분 수열의 마지막 수의 위치
ans = []

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j] and dp[j][0] + 1 > dp[i][0]:
            dp[i] = [dp[j][0]+1, j]
        if dp[i][0] > mx:
            mx = dp[i][0]
            last = i
            break

ans.append(nums[last])
pre = dp[last][1]
while pre != -1:
    ans.append(nums[pre])
    pre = dp[pre][1]
ans.reverse()
print(mx)
for i in ans:
    print(i, end=" ")
