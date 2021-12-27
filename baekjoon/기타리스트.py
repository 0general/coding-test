"""
https://www.acmicpc.net/problem/1495
"""
import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())

'''
# 상태 체크 
이전의 볼륨에서 더하거나 빼거나 2가지 방법으로 분기한다.
하지만 특정 값을 넘어가거나 0보다 작아지면 -1이 되어버린다.
n번째에서 최대값을 찾기 위해서는 (n-1)에서 만들 수 있는 모든 상태가 저장되어야 한다.
'''
# 0부터 m까지 모든 가능 볼륨을 저장해둔다.
dp = [[False]*(m+1) for _ in range(n)]  # i번째 연주 볼륨
p = list(map(int, input().split()))
vol = -1

a = s+p[0]
b = s-p[0]
if a <= m:
    dp[0][a] = True
    vol = max(vol, a)
if b >= 0:
    dp[0][b] = True
    vol = max(vol, b)

for i in range(n-1):
    vol = -1  # i+1번째 최대 볼륨
    for j in range(m, -1, -1):
        if dp[i][j]:  # (다음 i+1번째 연주에 영항을 주는 볼륨 : j)
            a = j + p[i+1]
            b = j - p[i+1]
            if a <= m:
                dp[i+1][a] = True
                vol = max(vol, a)
            if b >= 0:
                dp[i+1][b] = True
                vol = max(vol, b)
    if vol == -1:
        break


print(vol)
