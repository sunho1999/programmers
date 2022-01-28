from collections import deque


def solution(n, edge):
    answer = 0
    que = deque()
    matrix = [[] for i in range(n + 1)]  # 인접리스트로 노드 탐색
    visited = [0 for i in range(n + 1)]  # 방문노드 저장
    cost_node = [0 for i in range(n + 1)]  # 노드 방문할수록 count +=1
    for i in edge:
        a, b = i
        matrix[a].append(b)
        matrix[b].append(a)

    count = 1  # 초기 시작값 넣어주기
    for i in matrix[1]:
        que.append((i, count))
    visited[1] = 1

    while que:
        node, cost = que.popleft()
        if visited[node] == 0:
            visited[node] = 1
            cost_node[node] = cost
            cost += 1
            for i in matrix[node]:
                que.append((i, cost))

    for k in cost_node:
        if k == max(cost_node):
            answer += 1
    return answer