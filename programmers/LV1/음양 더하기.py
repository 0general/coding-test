def solution(absolutes, signs):
    sums = []
    for i, j in zip(absolutes, signs):
        if j == True:
            sums.append(i)
        else:
            sums.append(-i)
    return sum(sums)
