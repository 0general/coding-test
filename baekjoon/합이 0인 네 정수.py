"""
https://www.acmicpc.net/problem/7453
호석님 220129 방송 보면서 같이 함
두 개씩 열을 묶어서 새로운 열 2개를 만들어놓고 이분탐색으로 lower bound, upper bound 찾는 것도 있지만
여기서는 해쉬 써보자.
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
AB = {}
ans = 0

for i in range(n):
    for j in range(n):
        AB[arr[i][0] + arr[j][1]] = AB.get(arr[i][0] + arr[j][1], 0) + 1

for i in range(n):
    for j in range(n):
        ans += AB.get(-arr[i][2] - arr[j][3], 0)

print(ans)
