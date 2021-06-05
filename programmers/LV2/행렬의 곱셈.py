def solution(arr1, arr2):
    return [[sum([arr1[i][x]*arr2[x][j] for x in range(len(arr2))]) for j in range(len(arr2[0]))] for i in range(len(arr1))]
