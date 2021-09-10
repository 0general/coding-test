def solution(food_times, k):

    # k보다 작거나 같은 수 중에서 마지막 인덱스를 가리키는 최대 초 수를 이분탐색으로 구하라.

    l, r = 0, 100000000  # r = (2*10^13) / 200,000
    n = len(food_times)
    minor, check = 0, 0  # 모든 행에 빼야할 수, 마지막 인덱스를 가리킬 때의 초
    while l <= r:
        mid = (l+r)//2
        last = n*mid  # mid번 돌았을 때 마지막 인덱스를 가리킬 때의 초
        for i in food_times:
            tmp = i - mid
            if tmp < 0:
                last += tmp
        if last > k:
            r = mid - 1
        else:
            l = mid + 1
            minor, check = mid, last
    food_times = [f-minor for f in food_times]  # 갱신

    for i in range(n):
        if food_times[i] > 0 and check == k:
            return i + 1
        elif food_times[i] > 0:
            check += 1

    return -1
