"""
호석님 풀이

다이나믹 프로그래밍

dy[i] = 0~i에 대한 정답

마지막 i번 안티세포를 합칠 수 있는 방법은 logN가지밖에 없다.
한 번 합쳐질 때마다 크기가 2배씩 커진다

크기가 5인 두 세포가 합쳐지면 크기가 10이 되고 
크기가 10인 두 세포가 합쳐지면 크기가 20이 되니까 
커져봐야 많이 커지지 않는다. 

i세포가 합쳐질 수 있는 모든 구간을 찾은 다음에 다이나믹 값을 갱신하면 된다. 
2배씩 커지는 조건때문에 빨리 나오게 된다. 

"""


def solve(a, last, n):
    dy = [0 for _ in range(n)]
    dy[0] = 1
    accum = [dict() for _ in range(n)]
    for i in range(0, n):
        SUM, cnt = a[last + i], 1
        j = i
        accum[i][a[last+i]] = 1
        if i >= 1:
            dy[i] = dy[i-1]
        while j >= 1:
            if SUM not in accum[j-1]:
                break
            v = accum[j-1][SUM]
            cnt += v
            SUM *= 2  # 2배씩 커지는 조건
            j -= v
            if j-1 >= 0 and j - 1 < len(dy):
                dy[i] += dy[j-1]
            else:
                dy[i] += 1
            dy[i] %= 1000000007
            accum[i][SUM] = cnt
    return dy[n-1]


def solution(a, s):
    res = []
    last = 0
    for t in s:
        res.append(solve(a, last, t))
        last += t
    return res
