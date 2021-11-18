"""
https://www.acmicpc.net/problem/15656
"""


def BT(cnt, string):
    if cnt == m:
        print(string)
        return
    else:
        for i in range(n):
            BT(cnt+1, string+str(nums[i])+" ")


# 자연수 개수, 수열의 길이
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

BT(0, "")
