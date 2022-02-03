from collections import deque


def dfs(i, visited, computers):
    if visited[i] == 0:
        visited[i] = True
        for j in range(len(computers)):
            if j != i and computers[i][j] == 1:
                dfs(j, visited, computers)

def solution(n, computers):
    visited = [0 for i in range(n)]
    que = deque()
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(i, visited, computers)
            answer += 1
    return answer