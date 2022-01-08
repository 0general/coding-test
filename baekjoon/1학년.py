"""
https://www.acmicpc.net/problem/5557
"""
import sys

input = sys.stdin.readline

n = int(input())  # 3 <= n <= 100  숫자가 너무 크므로 백트래킹 불가 -> dp

# dp[idx][k] : idx 번째 항까지 숫자 k가 만들어질 수 있는 횟수
# 입력받을 마지막 수는 등식의 우항에 해당하는 숫자이므로 dp count에 들어갈 필요없음
dp = [[0]*21 for _ in range(n-1)]

ls = list(map(int, input().split()))

last = ls[-1]
dp[0][ls[0]] = 1

for i in range(1, n-1):  # 두 번째 항부터 끝에서 두 번째 항까지
    num2 = ls[i]
    for num1, x in enumerate(dp[i-1]):  # 앞 항에서 만들어질 수 있는 수와 그 가능성 검사
        if x != 0:  # 숫자 num1이 만들어질 수 있는 가능성의 수 x
            temp = num1+num2  # i번째 항에서 만들어질 수 있는 수
            if 0 <= temp <= 20:
                dp[i][temp] += x  # i-1번째 항에서 만들어진 수 num1에 num2만 더했으므로 가능성의 수도 동일
            temp = num1-num2  # i번째 항에서 만들어질 수 있는 수
            if 0 <= temp <= 20:
                dp[i][temp] += x  # i-1번째 항에서 만들어진 수 num1에 num2만 뺐으므로 가능성의 수도 동일

print(dp[-1][last])
