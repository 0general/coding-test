"""
https://www.acmicpc.net/problem/16496
"""
import sys

input = sys.stdin.readline

N = int(input())
arr = list(input().split())
arr.sort(key=lambda x: (x*10)[:10], reverse=True)
print(int(''.join(arr)))  # int로 변환 안 했다가 7번 틀림... 0000의 경우엔 0이 되어야 함
