'''
n = int(input())
dp = [[0]*n for _ in range(n)]
# [[0]*n]*n하면 배열은 만들어지지만 갱신이 동시에 일어남. 답이 틀림.
data = []
for i in range(n):
    data.append(float(input()))


for i in range(n):
    for j in range(i, n):
        if i == j:
            dp[i][j] = data[i]
        else:
            dp[i][j] = dp[i][j-1]*data[j]

print("%.3f" % (max(map(max, dp))))

#메모리 초과
'''
# 전형적인 DP문제
# https://www.acmicpc.net/problem/2670

n = int(input())
data = [float(input()) for _ in range(n)]

for i in range(1, n):
    data[i] = max(data[i], data[i-1]*data[i])

print("%.3f" % (max(data)))
