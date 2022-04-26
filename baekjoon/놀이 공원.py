"""
https://www.acmicpc.net/problem/1561
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
Mi = list(map(int, input().split()))

if N <= M:
    print(N)
else:
    s, e = 0, 60000000000

    ans = 0 # N명의 사람이 모두 놀이 기구에 탈 수 있는 시간
    people = 0 # ans 시간 동안 놀이 기구에 탈 수 있는 총 사람 수, N보다 클 수 있음에 유의할 것!
    while s <= e:
        time = (s+e)//2
        num = 0
        for i in range(M):
            num += (time // Mi[i])+1
        if num >= N:
            ans = time
            people = num
            e = time - 1
        else:
            s = time + 1

    mx = 0
    idx = 0

    for i in range(M-1, -1, -1):
        if ans % Mi[i] == 0:
            if people == N:
                print(i+1)
                break
            else: # 탈 수 있는 사람 수가 더 많은 경우에는 앞선 번호의 기구를 타야하기에
                people -= 1

'''
1987654321 2
15 14
-> 2

24 5
1 2 2 4 4
->4

'''
