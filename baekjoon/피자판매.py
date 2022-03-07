"""
https://www.acmicpc.net/problem/2632
"""
import sys

input = sys.stdin.readline

want = int(input())
m, n = map(int, input().split())
A = [int(input())]
for _ in range(m-1):
    A.append(A[-1]+int(input()))
B = [int(input())]
for _ in range(n-1):
    B.append(B[-1]+int(input()))


Asize = [0]*(1000001)
Bsize = [0]*(1000001)
Asize[0] = 1
Bsize[0] = 1
Asize[A[0]] += 1
Bsize[B[0]] += 1
for i in range(1, m):
    Asize[A[i]] += 1
    for j in range(i):
        num = A[i]-A[j]
        Asize[num] += 1
        if i == m-1:
            continue
        Asize[A[-1]-num] += 1  # 원형이라서 첫 조각과 마지막 조각이 연결되어 있음

for i in range(1, n):
    Bsize[B[i]] += 1
    for j in range(i):
        num = B[i]-B[j]
        Bsize[num] += 1
        if i == n-1:
            continue
        Bsize[B[-1]-num] += 1  # 원형이라서 첫 조각과 마지막 조각이 연결되어 있음

ans = 0
for i in range(want+1):
    if i > 1000000:
        break
    if Asize[i] == 0:
        continue
    if Bsize[want-i] != 0:
        ans += Asize[i]*Bsize[want-i]


print(ans)
