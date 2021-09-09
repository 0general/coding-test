'''
주어진 정점의 조건 (S,R,L)에 따라 현재 빛의 진행 방향을 바꾼다. 

grid는 ["SR","LR"]이런 식으로 주어진다.

호석님 풀이
'''


def solution(grid):
    n, m = len(grid), len(grid[0])
    answer = []
    visit = [[[0]*4 for _ in range(m)] for _ in range(n)]
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if visit[i][j][k]:
                    continue
                cnt = 0
                x, y, d = i, j, k
                while not visit[x][y][d]:
                    visit[x][y][d] = True
                    cnt += 1
                    x += dir[d][0]
                    y += dir[d][1]
                    '''
                    격자를 벗어나는 경우 반대로 이동해야 하는데 이게 사실 if문 조건이 2개가 들어간다. 
                    이걸 동시에 처리하는 방법이 밑의 방식이다.
                    '''
                    x = (x+n) % n
                    y = (y+m) % m
                    if grid[x][y] == 'L':
                        # L은 반시계 방향으로 회전하면 1이 빠지는 건데 +3을 한 뒤 나머지 4처리를 해줌으로써 동일 효과
                        d = (d+3) % 4
                    elif grid[x][y] == 'R':
                        d = (d+1) % 4
                answer.append(cnt)
    answer.sort()
    return answer
