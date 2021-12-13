"""
https://www.acmicpc.net/problem/2302
"""
n = int(input())
m = int(input())

# i번째 좌석표를 가진 사람이 왼쪽에 앉는 방법, i번째에 앉는 방법, 오른쪽에 앉는 방법
# 실제로 i번째 좌석이 채워지는데 영향을 끼치는 것은 왼쪽에 앉는 것과 원래 자리에 앉는 것이다.
# 오른쪽에 앉는 방법은 그저 기록용이라 생각하자.
dp = [[0, 0, 0] for _ in range(n+1)]
for i in range(m):
    num = int(input())
    dp[num][0], dp[num][2] = -1, -1

dp[0] = [0, 1, -1]
for i in range(1, n):
    if dp[i][0] != -1:  # 고정 좌석이 아닐 때
        dp[i][0] = dp[i-1][2] if dp[i-1][2] != -1 else 0
        dp[i][2] = dp[i-1][1] if dp[i+1][2] != -1 else 0
        if dp[i-1][2] != -1:  # 왼쪽에 앉아서 i번째 좌석까지 채우려면 i-1번째 사람은 오른쪽에 앉았어야 한다.
            dp[i][1] += dp[i-1][2]
    dp[i][1] += dp[i-1][1]

if dp[n-1][2] != -1 and dp[n][0] != -1:
    print(dp[n-1][1] + dp[n-1][2])
else:
    print(dp[n-1][1])
