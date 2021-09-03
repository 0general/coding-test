def solution(food_times, k):
    n = len(food_times)
    data = [0]*n
    for i, t in enumerate(food_times):
        data[i] = [i-1, i, t, i+1]  # pre,index,time,next
    data[0][0] = n-1
    data[n-1][3] = 0

    h = 0  # 현재 접시
    for i in range(k):
        data[h][2] -= 1
        if data[h][2] == 0:
            data[data[h][0]][3] = data[h][3]
            data[data[h][3]][0] = data[h][0]
        h = data[h][3]
        if data[h][2] == 0:
            return -1

    return data[h][1] + 1


# u = solution([3, 1, 2], 5)
# print(u)
