from collections import deque


# def solution(rectangle, characterX, characterY, itemX, itemY):
#     answer = 0
#     mapp = [[0 for _ in range(13)] for _ in range(13)]
#     renew_mapp = [[0 for _ in range(13)] for _ in range(13)]
#     visitied = [[0 for _ in range(13)] for _ in range(13)]
#     for i in range(len(rectangle)):
#         # print(rectangle[i])
#         for j in range(rectangle[i][0], rectangle[i][2] + 1):
#             for k in range(rectangle[i][1], rectangle[i][3] + 1):
#                 if mapp[j][k] == 0:
#                     mapp[j][k] = 1
#
#     def bfs(y, x):
#         que = deque()
#         que.append((y, x))
#         xy_list = []
#         dx = [-1, 1, 0, 0, 1, -1, -1, 1]
#         dy = [0, 0, -1, 1, 1, -1, 1, -1]
#
#         while que:
#             y1, x1 = que.popleft()
#             visitied[y1][x1] = 1
#             for i in range(8):
#                 x2 = x1 + dx[i]
#                 y2 = y1 + dy[i]
#                 if 0 <= x2 < len(mapp[0]) and 0 <= y2 < len(mapp):
#                     if mapp[y2][x2] == 1 and visitied[y2][x2] == 0:
#                         que.append((y2, x2))
#                     if mapp[y2][x2] == 0 and mapp[y1][x1] == 1:
#                         renew_mapp[y1][x1] = 1
#
#     for i in range(len(mapp)):
#         for j in range(len(mapp[0])):
#             if mapp[i][j] == 1:
#                 bfs(i, j)
#
#     def find_item(y, x, cnt):
#         answer_list = []
#         q = deque()
#         q.append((y, x, cnt))
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]
#         while q:
#             y1, x1, cntt = q.popleft()
#             new_visited[y1][x1] = 1
#
#             for i in range(4):
#                 y2 = y1 + dy[i]
#                 x2 = x1 + dx[i]
#                 if renew_mapp[y2][x2] == 2:
#                     answer_list.append(cntt)
#                 if 0 <= x2 < len(renew_mapp[0]) and 0 <= y2 < len(renew_mapp):
#                     if renew_mapp[y2][x2] == 1 and new_visited[y2][x2] == 0:
#                         q.append((y2, x2, cntt + 1))
#         return answer_list
#
#     renew_mapp[itemX][itemY] = 2
#     renew_mapp[characterX][characterY] = 3
#     print(renew_mapp)
#
#     new_visited = [[0 for _ in range(13)] for _ in range(13)]
#     a = find_item(characterX, characterY, 0)
#     print(new_visited)
#     print(a)
#     return answer
#
from collections import deque

def solution(rectangle, cx, cy, ix, iy):
    answer = 0
    maxX = 0
    maxY = 0

    for x,y,x2,y2 in rectangle:
        maxX = max(x2 * 2,maxX)
        maxY = max(y2 * 2,maxY)

    graph = [[0] * (maxX + 2) for _ in range(maxY + 2)]

    #1로 안쪽 다 칠하고
    for x,y,x2,y2 in rectangle:
        for i in range((x * 2),(x2 * 2) + 1):
            for j in range((y * 2),(y2 * 2) + 1):
                graph[j][i] = 1

    #전체 돌면서 주위 8개중에 하나가 0이면서 자기 자신이 1이면 2로 바꿈 테두리 경로
    for y in range(1,maxY + 1):
        for x in range(1,maxX + 1):
            for i in range(3):
                for j in range(3):
                    if graph[y + i - 1][x + j - 1] == 0 and graph[y][x] == 1:
                        graph[y][x] = 2
                        break

    dx = [1,0, 0, -1]
    dy = [0,1, -1, 0]
    queue = deque([(cx * 2,cy * 2,0)])
    ix *= 2
    iy *= 2
    while queue:
        x, y,length = queue.popleft()
        graph[y][x] = 1
        if x == ix and y == iy:
            answer = (length // 2)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[ny][nx] == 2:
                queue.append((nx,ny,length + 1))


    return answer