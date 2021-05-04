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
# greedy의 유형

# 준서가 버틸 수 있는 무게 K
n, k = map(int, input('N과 K을 순서대로 입력하시오 : ').split())
vklist = []

for i in range(n):
    a = list(map(int, input('무게와 가치를 순서대로 입력하시오 : ').split()))
    #[w, v]
    vklist.append(a)

max_value = 0  # 최종 가치의 최댓값

vklist.sort(key=lambda x: x[0], reverse=True)  # 무게에 따라 정렬

for j in range(len(vklist)):
    whap = 0  # 무게 합
    vhap = 0  # 가치 합
    check = j
    while whap < k:
        if check + 1 < len(vklist):
            if whap + vklist[check][0] <= k:
                if vklist[check][1] > vklist[check+1][1]:
                    whap += vklist[check][0]
                    vhap += vklist[check][1]
                else:
                    check += 1
                    whap += vklist[check][0]
                    vhap += vklist[check][1]
            else:
                check += 1
        elif check + 1 == len(vklist):
            if whap + vklist[check][0] <= k:
                whap += vklist[check][0]
                vhap += vklist[check][1]
            else:
                break
        else:
            break
    if vhap > max_value:
        max_value = vhap

print(max_value)
