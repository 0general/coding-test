def solution(n, words):
    st = set()
    for index in range(len(words)):
        if index == 0:
            st.add(words[index])
        elif words[index-1][-1] == words[index][0] and words[index] not in st:
            st.add(words[index])
        else:
            return [index % n+1, index//n + 1]
    return [0, 0]
