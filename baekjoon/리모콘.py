"""
https://www.acmicpc.net/problem/1107
"""
import sys


def bf(string):
    if int(string) < 0:
        return False
    for s in string:
        if not button[int(s)]:
            return False
    return True


# 이동하려는 채널
N = input()
n = int(N)
# 고장난 버튼 개수
m = int(input())
# 누를 수 있는 버튼
button = [True]*10
minor = abs(n-100)
if minor == 0:
    print(minor)
else:
    if m == 0:  # 버튼을 전부 누를 수 있을 때
        print(min(minor, len(N)))  # 위아래로 이동하든가, 채널을 누르든가
        sys.exit()
    for i in list(map(int, input().split())):
        button[i] = False
    if m == 10:  # 버튼을 전혀 누를 수 없을 때
        print(minor)
    else:
        i = 0  # i=1 로 초기화 했다가 가려는 채널이 0인 경우를 찾지 못해서 3번 틀림
        while True:
            a = str(n+i)
            b = str(n-i)
            if bf(b):
                minor = min(minor, len(b) + i)
                break
            if bf(a):
                minor = min(minor, len(a) + i)
                break
            i += 1
        print(minor)

'''
1555
8
0 1 3 4 5 6 7 9
670
    
101
3
4 5 6
1
    
162
9
0 1 3 4 5 6 7 8 9
62
    
10
9
1 2 3 4 5 6 7 8 9
11
    
1
10
0 1 2 3 4 5 6 7 8 9  
99
    
1
1
1
2
    
0
9
1 2 3 4 5 6 7 8 9
1
    
101
0
1
    
100000
9
0 1 2 3 4 5 6 7 8
6
    
1
10
0 1 2 3 4 5 6 7 8 9
99
    
1111
9
1 2 3 4 5 6 7 8 9 
1011
    
2229
6
4 5 6 7 8 9
5
    
10
1
0
2
    
0
10
0 1 2 3 4 5 6 7 8 9
100
    
9
8
0 3 4 5 6 7 8 9
4
    
0
3
0 1 2
4
'''
