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
