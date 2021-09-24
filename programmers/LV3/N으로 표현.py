def solution(N, number):
    num = [0, {N}]
    for i in range(2, 9):  # 2~8
        temp = {int(str(N)*i)}
        for j in range(1, i//2+1):
            for s1 in num[j]:
                for s2 in num[i-j]:
                    temp.add(s1+s2)
                    if s1-s2 != 0:
                        temp.add(abs(s1-s2))
                    temp.add(s1*s2)
                    if s1//s2 != 0:
                        temp.add(s1//s2)
                    if s2//s1 != 0:
                        temp.add(s2//s1)
        num.append(temp)
    for su in range(1, 9):
        if number in num[su]:
            return su

    return -1
