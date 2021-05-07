def solution(n, t, m, p):
    big = ['0', '1', '2', '3', '4', '5', '6', '7',
           '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    su = m*(t-1) + p
    number = [big[x] for x in range(n)]

    for i in range(n, su):
        check = []
        u = i
        while u > 0:
            check.append(big[u % n])
            u = u//n
        check.reverse()
        number.extend(check)
        if len(number) > su:
            break

    answer = ''

    for k in range(t):
        dap = (p-1)+k*m
        answer += number[dap]

    return answer
