"""
https://www.acmicpc.net/problem/14225
"""
import sys


def sum_subsequence(sidx, sum):
    if sidx == n:
        return
    number[sum+arr[sidx]] = True
    sum_subsequence(sidx+1, sum+arr[sidx])
    sum_subsequence(sidx+1, sum)


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

number = [False]*(2000001)

sum_subsequence(0, 0)
for i in range(1, len(number)):
    if number[i] == False:
        print(i)
        break
