from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())  # 편의점 개수
    arr = []
    q = deque()
    flag = False
    visited = [False]*(n+2)
    arr = [list(map(int, input().split()))]
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    temp.sort(key=lambda x: abs(arr[0][0]-x[0]
                                ) + abs(arr[0][1]-x[1]))  # 거리순 정렬
    arr += temp
    arr.append(list(map(int, input().split())))
    for i in range(1, n+2):
        dist = abs(arr[0][0]-arr[i][0]) + abs(arr[0][1]-arr[i][1])
        if dist//50 < 20 or (dist//50 == 20 and dist % 50 == 0):
            q.append(i)
            visited[i] = True
            if i == n+1:
                print("happy")
                flag = True
    if flag:
        continue
    while q:
        now = q.popleft()
        # 락 페스티벌의 위치가 어디에 위치하고 있는지 모르기 때문에 모두 다 돌아봐야 한다.
        for i in range(1, n+2):
            if visited[i]:
                continue
            dist = abs(arr[now][0]-arr[i][0]) + abs(arr[now][1]-arr[i][1])
            if dist//50 < 20 or (dist//50 == 20 and dist % 50 == 0):
                q.append(i)
                visited[i] = True
                if i == n+1:
                    print("happy")
                    flag = True
        if flag:
            break
    if flag:
        continue
    print("sad")
