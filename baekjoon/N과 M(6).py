"""
https://www.acmicpc.net/problem/15655
"""
import sys


def BT(i, cnt, string):
    if cnt == m and string not in ans:
        ans.add(string)
        print(string)
        return
    elif cnt != m and m-cnt > n-i-1:
        return
    for j in range(i+1, n):
        BT(j, cnt+1, string+" "+str(nums[j]))


input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = set()
for i in range(n):
    BT(i, 1, str(nums[i]))
