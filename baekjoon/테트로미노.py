"""
https://www.acmicpc.net/problem/14500
"""
n, m = map(int, input().split())
poly = [list(map(int, input().split())) for _ in range(n)]
visit = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, cnt, hap, big, visit):  # 현재 위치 i,j / dfs count, 최대값 구하기 위한 합
    # 현재 위치에서 cnt == 4 이면 hap에 더하고 big이랑 max 따져서 return
    if cnt > 4:
        return big
    if cnt == 4:
        big = max(big, hap+poly[i][j])
    else:
        for k in range(4):
            nowx = i+dx[k]
            nowy = j+dy[k]
            if 0 <= nowx < n and 0 <= nowy < m and not visit[nowx][nowy]:
                if cnt == 2:
                    visit[nowx][nowy] = True
                    big = dfs(i, j, cnt+1, hap+poly[nowx][nowy], big, visit)
                    visit[nowx][nowy] = False
                visit[nowx][nowy] = True
                big = dfs(nowx, nowy, cnt+1, hap+poly[i][j], big, visit)
                visit[nowx][nowy] = False
    return big


big = -1
visit = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        big = dfs(i, j, 1, 0, big, visit)
        visit[i][j] = False

print(big)
