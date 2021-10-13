"""
https://www.acmicpc.net/problem/11723
"""
import sys

input = sys.stdin.readline

def add_x(x):
    s.add(x)
    return s

def remove_x(x):
    s.discard(x)
    return s

def check(x):
    if x in s:
        print(1)
    else:
        print(0)
    return s

def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)
    return s

def all_s():
    return {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"} #set(list(map(str,range(1, 21)))) 시간 초과나서 바꿔봄

def empty_s():
    return set() # s.clear()를 하고 s를 반환하면 불필요한 시간 추가

dic = {"add":add_x, "remove":remove_x, "check":check, "toggle":toggle, "all":all_s, "empty":empty_s}
s = set()
m = int(input())
for _ in range(m):
    query = list(input().split())
    if len(query) == 1: #all or empty
        s = dic[query[0]]()
    else:
        s = dic[query[0]](query[1])
