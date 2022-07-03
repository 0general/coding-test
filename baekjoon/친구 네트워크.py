"""
https://www.acmicpc.net/problem/4195
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100010)


def union(a, b, networks, friends):
    a = find(a, networks, friends)
    b = find(b, networks, friends)
    if a < b:
        networks[b] = a
        friends[a] += friends[b]
        return friends[a]
    elif a == b:
        return friends[a]
    else:
        networks[a] = b
        friends[b] += friends[a]
        return friends[b]


def find(a, networks, friends):
    if a not in networks:
        networks[a] = a
        friends[a] = 1
    if networks[a] == a:
        return a
    else:
        networks[a] = find(networks[a], networks, friends)
    return networks[a]


for _ in range(int(input())):
    friends = dict()
    networks = dict()
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        print(union(a, b, networks, friends))
