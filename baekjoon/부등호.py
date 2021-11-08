"""
https://www.acmicpc.net/problem/2529
"""
import sys


# idx 자체가 숫자, cnt는 현재 string에 들어있는 숫자 수이자, 확인해야 할 다음 부등호의 인덱스를 가르킨다.
def BT(idx, cnt, string):
    if len(answer) >= 1:  # 모든 경우가 아닌 가장 크거나 가장 작은 것 하나씩만 필요하기에 구해지면 모든 함수 종료
        return
    if cnt == k:
        answer.append(string)
        return
    if sign[cnt] == '<':
        for j in range(idx+1, 10):  # 현재 마지막 숫자보다 큰 숫자들을 검사
            if visit[j] == 0:
                visit[j] = 1
                BT(j, cnt+1, string+str(j))
                visit[j] = 0
            if len(answer) >= 1:
                break
    else:
        for j in range(idx-1, -1, -1):  # 현재 마지막 숫자보다 작은 숫자들을 검사
            if visit[j] == 0:
                visit[j] = 1
                BT(j, cnt+1, string+str(j))
                visit[j] = 0
            if len(answer) >= 1:
                break


input = sys.stdin.readline
k = int(input())
visit = [0]*(10)
sign = input().rstrip().split()

answer = []
for i in range(9, -1, -1):
    if len(answer) == 1:
        break
    visit[i] = 1
    BT(i, 0, str(i))  # number, cnt, string
    visit[i] = 0

print(answer.pop())

for i in range(10):
    if len(answer) == 1:
        break
    visit[i] = 1
    BT(i, 0, str(i))
    visit[i] = 0

print(answer.pop())
