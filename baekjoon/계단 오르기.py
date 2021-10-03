"""
https://www.acmicpc.net/problem/2579
"""
import sys

input = sys.stdin.readline

n = int(input())
stair = [[0, 0]]
for i in range(n):
    stair.append(int(input()))

ok = True
for i in range(1, n+1):
    k = stair[i]
    if i == 1:
        stair[i] = [k, 0]
    elif i == 2:  # 두번째 계단은 유일하게 앞선 계단에서 제한이 존재하지 않는다. 첫번째 계단에서 연달아 선택 가능하기 때문
        stair[i] = [max(stair[i-1])+k, max(stair[i-2])+k]
    else:
        # 세번째 계단부터는 앞선 계단에서 선택할 수 있는 가짓수가 제한되어있다.
        # stair[i-1]의 첫번째 요소는 i-2번째 계단을 밟고 완성된 가중치이므로 선택 불가하고,
        # 이전 계단을 밟고 이번 계단을 밟으려면 이전 계단은 이전 계단을 선택한 것이 아니어야 한다.
        # [i-1번째 계단을 밟은 경우, i-2번째 계단을 밟은 경우]
        stair[i] = [stair[i-1][1]+k, max(stair[i-2])+k]

print(max(stair[n]))
