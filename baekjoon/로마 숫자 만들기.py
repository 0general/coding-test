"""
https://www.acmicpc.net/problem/16922
"""


def BT(cnt, num, index):
    global answer
    if cnt == n:
        if not visited[num]:
            visited[num] = True
            answer += 1
            return
    else:
        for i in range(index, len(size)):
            BT(cnt+1, num+size[i], i)


visited = [False]*(1001)  # 50*20 까지 가능
n = int(input())
size = [1, 5, 10, 50]
answer = 0
BT(0, 0, 0)
print(answer)
