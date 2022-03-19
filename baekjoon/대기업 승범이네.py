"""
https://www.acmicpc.net/problem/17831
"""
import sys
sys.setrecursionlimit(200010)
input = sys.stdin.readline

n = int(input())
dp = [[0, 0] for _ in range(n+1)]
arr = [[] for _ in range(n+1)]

for i, p in enumerate(list(map(int, input().split())), start=2):
    arr[p].append(i)
ability = [0] + list(map(int, input().split()))


def dfs(root):
    if len(arr[root]) == 0:
        return dp[root]

    for c in arr[root]:
        child = dfs(c)
        dp[root][1] += max(child)  # root가 멘토링 참여하지않을 때는 자식 노드들의 최대값들 더해주면 된다.

    for c in arr[root]:  # root와 멘토링을 묶을 c를 선택
        num = ability[root]*ability[c] + dp[root][1]  # root가 멘토링에 참여하는 경우
        if dp[c][0] > dp[c][1]:  # 자식 노드 c가 자신의 자식과 멘토링으로 묶여있는 경우가 dp[root][1]에 들어있다면
            num += dp[c][1] - dp[c][0]  # 그 값을 빼주고 c가 자식들과 멘토링으로 안 묶이는 경우를 더해줌
        dp[root][0] = max(dp[root][0], num)
    return dp[root]


print(max(dfs(1)))
