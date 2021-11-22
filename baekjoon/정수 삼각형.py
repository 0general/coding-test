"""
https://www.acmicpc.net/problem/1932
"""
import sys

input = sys.stdin.readline
n = int(input())
state = []
for i in range(n):
    if i == 0:
        state.append(int(input()))
    else:
        arr = list(map(int, input().rstrip().split()))
        for j in range(i+1):
            if j == 0:
                arr[j] += state[0]
            elif j == i:
                arr[j] += state[j-1]
            else:
                arr[j] += max(state[j], state[j-1])
        state = arr

print(max(state))
