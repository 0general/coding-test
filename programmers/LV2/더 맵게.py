from heapq import *
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)


def solution(scoville, K):
    heapify(scoville)
    answer = 0

    while len(scoville):
        i = heappop(scoville)
        if i < K and not len(scoville):
            return -1
        elif i < K:
            j = heappop(scoville)
            heappush(scoville, i+(j*2))
            answer += 1
        else:
            break

    return answer
