
"""
https://www.acmicpc.net/problem/10819
"""
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

ans = 0
for com in list(permutations(num, n)):
    temp = 0
    for j in range(1, n):
        temp += abs(com[j]-com[j-1])
    ans = max(ans, temp)

print(ans)

'''
i, j = 0, n-1
ans = []
temp = []
j_first = True
while i < j:
    if i == 0 and j == n-1:
        if abs(num[i]) > abs(num[j]):
            j_first = False
    if j_first:
        temp.append(num[j])
        temp.append(num[i])
    else:
        temp.append(num[i])
        temp.append(num[j])
    i += 1
    j -= 1
    if i == j:
        ans.append(num[i])
        break
if ans:
    ans += temp
else:
    ans += [temp[-1]] + temp[:-1]

cnt = 0
for u in range(1, n):
    cnt += abs(ans[u]-ans[u-1])

print(cnt)
'''
"""
반례 
5
-1 -1 0 -3 -4 

"""
