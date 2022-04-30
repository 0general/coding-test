"""
https://www.acmicpc.net/problem/14889
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = [i for i in range(1,n+1)]
start = []
link = []

abil = [list(map(int, input().split())) for _ in range(n)]

def select(i,num,ls): # 팀 나누기
    if num == n//2:
        start.append(tuple(ls)) #ls는 mutable이라 계속 변경되는 것을 방지한다.
        temp = []
        for k in range(1,n+1):
            if k not in set(ls):
                temp.append(k)
        link.append(tuple(temp))
        return
    if i >= n or n-i < n//2 - num:
        return
    ls.append(arr[i])
    select(i+1,num+1,ls)
    ls.pop()
    select(i+1,num,ls)

def skill_sum(ls):
    ans = 0
    for i in ls:
        for j in ls:
           ans += abil[i-1][j-1]
    return ans


select(0,0,[]) # 팀을 미리 분배해놓는다.

mx = 2000
for s, l in zip(start, link):
    x = abs(skill_sum(s) - skill_sum(l))
    if x == 0:
        mx = 0
        break
    if x < mx:
        mx = x

print(mx)

