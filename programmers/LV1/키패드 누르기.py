import numpy


def solution(numbers, hand):
    pwd = numpy.array([[4, 1], [4, 3]])
    where = numpy.array([[4, 2], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3],
                        [3, 1], [3, 2], [3, 3]])
    answer = ''
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'
            pwd[0] = where[numbers[i]]
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
            pwd[1] = where[numbers[i]]
        else:
            Rp = sum(abs(where[numbers[i]] - pwd[1]))
            Lp = sum(abs(where[numbers[i]] - pwd[0]))
            if Rp > Lp:
                answer += 'L'
                pwd[0] = where[numbers[i]]
            elif Rp < Lp:
                answer += 'R'
                pwd[1] = where[numbers[i]]
            else:
                if hand == "right":
                    answer += 'R'
                    pwd[1] = where[numbers[i]]
                else:
                    answer += 'L'
                    pwd[0] = where[numbers[i]]
    return answer
