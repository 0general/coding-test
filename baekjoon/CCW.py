"""
https://www.acmicpc.net/problem/11758
"""
# 외적 이용
# 좌표는 2차원 평면(xy좌표축) 위에 존재
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 외적은 오른손 법칙에 의해 xy평면에 수직인 방향, 즉 [0,0,abx]의 꼴로 존재
a = [x2-x1, y2-y1, 0]  # a벡터
b = [x3-x1, y3-y1, 0]  # b벡터
abx = a[0]*b[1]-a[1]*b[0]

if abx == 0:  # 0이면 평행
    print(0)
elif abx > 0:  # 오른손 법칙에 의해 반시계방향이면 양수
    print(1)
else:  # 시계방향이면 음수
    print(-1)
