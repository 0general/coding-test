from collections import Counter


def solution(lottos, win_nums):
    pb = (Counter(lottos))[0]
    pf = len(set(win_nums) & set(lottos))
    dap = [pb+pf, pf]
    answer = []
    for i in range(2):
        if dap[i] == 6:
            answer.append(1)
        elif dap[i] == 5:
            answer.append(2)
        elif dap[i] == 4:
            answer.append(3)
        elif dap[i] == 3:
            answer.append(4)
        elif dap[i] == 2:
            answer.append(5)
        else:
            answer.append(6)

    return answer
