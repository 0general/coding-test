"""
https://www.acmicpc.net/problem/11062
pypy로만 통과, python3로는 시작과 동시에 시간초과
"""
import sys

input = sys.stdin.readline
# sys.setrecursionlimit(500010) # 이것 쓰면 오히려 메모리 초과로 실패


def score(i, j):
    if dp[i][j] != 0:
        return dp[i][j]
    if i == j:
        dp[i][j] = arr[i]
        return dp[i][j]
    else:
        # i를 고르든 j를 고르든 다음 배열에서의 최대 점수차는 다음 플레이어의 몫이 된다.
        dp[i][j] = max(arr[i]-score(i+1, j), arr[j]-score(i, j-1))
        return dp[i][j]


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    # i부터 j까지의 배열 속에서 가질 수 있는 점수 차
    dp = [[0 for _ in range(n)] for _ in range(n)]
    diff = score(0, n-1)
    print((sum(arr)+diff)//2)
