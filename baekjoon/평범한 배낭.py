'''
https://www.acmicpc.net/problem/12865

- 여행에 필요하다고 생각하는 N개의 물건 
- 각 물건의 무게 W, 가치 V(준서의 즐김 수치)
- 준서가 배낭에 최대한 넣을 수 있는 무게 K

준서가 최대한 즐거운 여행을 하기 위해
배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자

- 첫 줄에 물품의 수 N (1이상 100이하), 준서가 버틸 수 있는 무게 K (1 이상 10만 이하)
- 두번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1이상 10만 이하)와 해당 물건의 가치 V(0이상 1000이하)

입력으로 주어지는 모든 수는 정수

'''

# 준서가 버틸 수 있는 무게 K
n, k = map(int, input().split())
mat = [[0]*(k+1) for _ in range(n+1)]
item = [[0, 0]]
for i in range(n):
    item.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= item[i][0]:  # 지금 들고있는 물건도 넣기가 가능해질 때
            mat[i][j] = max(mat[i-1][j], mat[i-1][j-item[i][0]]+item[i][1])
        else:
            mat[i][j] = mat[i-1][j]

print(mat[-1][-1])
