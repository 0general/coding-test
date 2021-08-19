def solution(operations):
    answer = []
    for opr in operations:
        op = opr.split()
        if op[0] == "I":
            answer.append(int(op[1]))
            answer.sort()
        else:
            if len(answer) == 0:
                continue
            if int(op[1]) > 0:
                answer.pop()
            else:
                answer = answer[1:]

    return [answer[-1], answer[0]] if len(answer) != 0 else [0, 0]



'''
import heapq

def solution(operations):
    h = []

    for i in operations:
        a, b = i.split()
        if a == 'I':
            heapq.heappush(h, int(b))
        else:
            if len(h) > 0:
                if b == '1':
                    h.pop(h.index(heapq.nlargest(1, h)[0]))
                else:
                    heapq.heappop(h)

    if len(h) == 0:
        return [0, 0]
    else:
        return [heapq.nlargest(1, h)[0], h[0]]

'''