def solution(citations):
    citations.sort(reverse=True)
    for i, v in enumerate(citations):
        if i+1 >= len([j for j in citations if j >= i+1]):
            return min(i+1, v)

    return 0
