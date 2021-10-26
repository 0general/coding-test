"""
https://programmers.co.kr/learn/courses/30/lessons/43162
"""
from collections import deque


def bfs(q, computers, visited):
    while q:
        now = q.popleft()
        for ix in range(len(computers)):
            if ix != now and not visited[ix] and computers[now][ix]:
                visited[ix] = True
                q.append(ix)


def solution(n, computers):
    answer = 0
    visited = [False]*n
    q = deque()
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            q.append(i)
            answer += 1
            bfs(q, computers, visited)

    return answer
