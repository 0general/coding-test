def dfs(i, computers, visited, stack):  # 각 항 검색
    result = stack
    if type(result) == list:
        if not visited[i]:  # 아직 방문하지 않은 노드
            visited[i] = True
            result.append(i)
            for j in range(len(computers)):
                if i == j:
                    continue
                if computers[i][j] == 1 and not visited[j]:
                    result = dfs(j, computers, visited, result)
    else:
        return -1
    if len(stack) == 0:
        return -1
    return result


def solution(n, computers):

    visited = [False for _ in range(n)]
    network = []

    for i in range(n):
        stack = []
        a = dfs(i, computers, visited, stack)
        if a != -1:
            network.append(a)
    print(network)

    return len(network)
