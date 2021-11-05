"""
https://www.acmicpc.net/problem/2225
"""
N, K = map(int, input().split())
dp = [[1]*(N+1) for i in range(K+1)]  # k번의 연산으로 만들수 있는 수 n

for k in range(2, K+1):
    for n in range(1, N+1):  # 표를 한번 그려볼 것.
        # k 번의 연산으로 n-1이 만들어지는 경우 1만 더하면 된다.
        # k-1 번의 연산으로 n이 만들어지는 경우 0(덧셈에 대한 항등원)을 더하면 된다.
        # 정확하게 따지자면 dp[k-1][0] ~ dp[k-1][n]까지를 모두 더해야하는 것(뒤에 더해질 수들은 dp[k-1][n-i] + i로 정해져 있다.)인데
        # dp[k][n-1]에서 이미 dp[k-1][0]부터 dp[k-1][n-1]까지를 모두 구해놨기 때문에 가져다 쓰면 된다.
        dp[k][n] = (dp[k][n-1] + dp[k-1][n]) % 1000000000

print(dp[K][N])
