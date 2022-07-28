from collections import deque


def bfs(que, maps):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while que:
        x, y, cnt = que.popleft()  # x,y좌표
        visited[x][y] = cnt
        cnt += 1
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < len(maps) and 0 <= ay < len(maps[0]):
                if visited[ax][ay] == 0 and maps[ax][ay] == 1:
                    visited[ax][ay] = cnt
                    que.append((ax, ay, cnt))
    return visited[-1][-1]


def solution(maps):
    answer = 0
    que = deque()
    que.append((0, 0, 1))
    answer = bfs(que, maps)
    if answer == 0:
        return -1
    return answer

# [[1, 0, 1, 1, 1],
#  [1, 0, 1, 0, 1],
#  [1, 0, 1, 1, 1],
#  [1, 1, 1, 0, 1],
#  [0, 0, 0, 0, 1]]