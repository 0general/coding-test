"""
https://programmers.co.kr/learn/courses/30/lessons/43163
"""
from collections import Counter
from collections import deque

def solution(begin, target, words):
    # 모든 단어의 개수 n
    n = len(words) + 1
    # 인덱스 가정. begin = 0, words = 1~n-2
    word_list = [begin] + words
    visited = [False]*n
    graph = [[] for _ in range(n)] 
    for i in range(n-1): 
        # graph에 자기자신과 한 개의 알파벳 차이만 나는 단어를 인접하다고 판단 graph에 삽입
        now = Counter(word_list[i])
        for j in range(i+1,n):
            if len(now - Counter(word_list[j])) == 1:
                graph[i].append(j)
                graph[j].append(i)
    graph = list(map(sorted, graph))
    q = deque()
    visited[0] = True
    q.append((0,0))
    while q:
        now, cnt = q.popleft()
        print(word_list[now])
        if word_list[now] == target: 
            return cnt
        for idx in graph[now]:
            if not visited[idx]:
                visited[idx] = True
                q.append((idx,cnt+1))
    return 0