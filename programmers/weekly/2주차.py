def solution(scores):
    answer = ''
    n = len(scores)
    for i in range(n):
        a = [scores[j][i] for j in range(n)]
        hap = sum(a)
        ck = scores[i][i]
        mx = max(a)
        mn = min(a)
        if (ck == mx or ck == mn) and a.count(ck) == 1:
            hap -= ck
            mean = hap/(n-1)
        else:
            mean = hap/n
        print("평균 : ", mean)
        if mean >= 90:
            answer += 'A'
        elif mean >= 80:
            answer += 'B'
        elif mean >= 70:
            answer += 'C'
        elif mean >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer
