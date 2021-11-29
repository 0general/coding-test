"""
https://www.acmicpc.net/problem/16935
"""
import sys


def up_and_down():
    n = len(graph)
    for i in range(n//2):
        graph[i], graph[-(i+1)] = graph[-(i+1)], graph[i]


def right_and_left():
    n, m = len(graph), len(graph[0])
    for i in range(n):
        for j in range(m//2):
            graph[i][j], graph[i][-(j+1)] = graph[i][-(j+1)], graph[i][j]


def turn_right():
    global graph
    n, m = len(graph), len(graph[0])
    arr = []
    for j in range(m):
        temp = []
        for i in range(n-1, -1, -1):
            temp.append(graph[i][j])
        arr.append(temp)
    graph = arr


def turn_left():
    global graph
    n, m = len(graph), len(graph[0])
    arr = []
    for j in range(m-1, -1, -1):
        temp = []
        for i in range(n):
            temp.append(graph[i][j])
        arr.append(temp)
    graph = arr


def group_turn_right():
    n, m = len(graph)//2, len(graph[0])//2
    for i in range(n):
        for j in range(m):
            graph[i][j], graph[i][j+m], graph[i+n][j+m], graph[i +
                                                               n][j] = graph[i+n][j], graph[i][j], graph[i][j+m], graph[i+n][j+m]


def group_turn_left():
    n, m = len(graph)//2, len(graph[0])//2
    for i in range(n):
        for j in range(m):
            graph[i][j], graph[i][j+m], graph[i+n][j+m], graph[i +
                                                               n][j] = graph[i][j+m], graph[i+n][j+m], graph[i+n][j], graph[i][j]


input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
order = {1: up_and_down, 2: right_and_left, 3: turn_right,
         4: turn_left, 5: group_turn_right, 6: group_turn_left}

for i in list(map(int, input().rstrip().split())):
    order[i]()

for i in range(len(graph)):
    print(*graph[i])
