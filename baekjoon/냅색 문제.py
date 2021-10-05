'''
https://www.acmicpc.net/problem/1450
'''
"""
https://www.acmicpc.net/problem/1450
"""

import sys
input = sys.stdin.readline

# n개의 물건, 넣을 수 있는 최대 c의 무게
n, c = map(int, input().split())
goods = list(map(int, input().split()))
goods.sort()

dp = [0] * (c+1)  # 인덱스 : 무게, 값 : 개수
dp[0] = 1
l, r = 0, n-1
ans = 0
while l < r:
    mid = (l+r)//2
    if goods[mid] <= c:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

for good in goods[:ans+1]:
    dp[good] += 1


print(sum(dp[:ans+1]))
