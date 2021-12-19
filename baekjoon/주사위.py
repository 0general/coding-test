"""
https://www.acmicpc.net/problem/1041
"""
import sys

input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

if N == 1:
    print(sum(num)-max(num))
else:
    h2 = {0: [0, 1, 2, 3], 1: [0, 4, 5, 8], 2: [1, 4, 7, 11],
          3: [2, 5, 6, 9], 4: [3, 6, 7, 10], 5: [8, 9, 10, 11]}
    h3 = {0: [0, 1, 2, 3], 1: [0, 1, 4, 5], 2: [0, 3, 4, 7],
          3: [1, 2, 5, 6], 4: [2, 3, 6, 7], 5: [4, 5, 6, 7]}
    hap2 = [0]*12
    hap3 = [0]*8
    for i in range(6):
        for ni in h2[i]:
            hap2[ni] += num[i]
        for ni in h3[i]:
            hap3[ni] += num[i]
    answer = (5*N-6)*(N-2)*min(num)
    answer += (8*N-12)*min(hap2)
    answer += 4*min(hap3)
    print(answer)
