"""
https://www.acmicpc.net/problem/2294
"""
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
dp = [0]*(100000+1)  # index원을 만들기 위한 최소 동전의 개수
# 조건 제대로 안 읽고 dp범위를 K+1로 했다가 인덱스 에러로 틀렸었다. 동전의 범위로 설정해야
coin = []
q = deque()
for i in range(N):
    number = int(input())
    # 가치가 같은 동전 여러개가 들어올 수 있으나 최소 동전의 개수를 구하는 거라 가치가 같으면 하나로 친다.
    if dp[number] == 0:
        coin.append(number)
        dp[number] = 1
        q.append(number)

coin.sort()  # 동전이 반드시 크기 순으로 들어온다는 말이 없어서 크기 순 정렬

while q:
    now = q.popleft()
    for c in coin:
        temp = now + c
        if temp <= K and dp[temp] == 0:  # 최소 동전의 개수니까 종류는 상관없다.
            dp[temp] = dp[now]+1
            q.append(temp)
if dp[K] == 0:
    print(-1)  # 조건 똑바로 읽자. 이거 처리 안해서 두 번 틀림
else:
    print(dp[K])
