"""
https://www.acmicpc.net/problem/15666
"""
import sys

input = sys.stdin.readline

# 중복조합
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

ans_list = set()

def dfs(idx,num,string):
    if num == m:
        if string not in ans_list:
            ans_list.add(string)
            print(string)
        return
    if idx >= n:
        return
    # idx번째 수를 포함하든가
    dfs(idx, num+1, string+str(arr[idx])+" ")
    # idx번째 수를 포함하지 않든가
    dfs(idx+1,num,string)

dfs(0,0,"")