"""
https://www.acmicpc.net/problem/1959
"""
# N 크기가 매우 크므로 그냥 계산하는 것이 훨씬 빠르다
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

# 껍데기 개수
husk = min((M-1)//2, (N-1)//2)
ans = husk*4
m, n = M-husk*2, N-husk*2
if min(m, n) == 1:  # 한 줄
    if n >= m:  # 가로가 더 길다
        print(ans)
        print(M-husk, N-husk)
    else:
        print(ans + 1)
        print(M-husk, husk+1)
else:  # 2일 때
    if n >= m:
        print(ans+2)
        print(husk+2, husk+1)
    else:
        print(ans+3)
        print(husk+2, N-husk-1)


# 메모리 초과 N과 M이 최대 21억임
# visited = [[0 for _ in range(N)] for _ in range(M)]
# dir = [(0,1),(1,0),(0,-1),(-1,0)]
# d = 0

# num = 0
# i,j = 0,0

# def snail(i,j):
#     global d, num
#     nx, ny = i + dir[d][0], j + dir[d][1]
#     if nx < 0 or ny < 0 or nx >= M or ny >= N or visited[nx][ny]:
#         d = (d+1)%4
#         nx, ny = i + dir[d][0], j + dir[d][1]
#         num += 1
#     if not visited[nx][ny]:
#         visited[nx][ny] = True
#         return nx,ny
#     num -= 1
#     return i,j

# visited[0][0] = True
# while True:
#     nx, ny = snail(i,j)
#     if i == nx and j == ny:
#         break
#     i = nx
#     j = ny

# print(num)
# print(i+1,j+1)
