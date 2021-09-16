def solution(n, times):
    # 수가 매우 크므로 이분탐색을 당연히 생각해야한다.
    # 걸리는 최소시간을 return해야하므로 start, end, mid는 시간
    # 시간 범위는 0부터 가장 오래 걸리는 검색대에서 모든 인원이 검사받은 경우
    times.sort()
    start = 0
    end = times[-1]*n
    while start < end:
        mid = (start + end)//2
        su = 0
        for i in times:
            su += mid//i
        if su >= n:
            end = mid
        else:
            start = mid+1
    return start
