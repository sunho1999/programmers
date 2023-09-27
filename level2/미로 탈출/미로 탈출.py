from collections import deque

def solution(maps):
    def find_L(y, x):
        que = deque()
        que.append((y, x, 0))
        while que:
            y, x, cnt = que.popleft()
            if maps[y][x] == "L":
                yxc = [y, x, cnt]
                return yxc
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < len(maps[0]) and 0 <= yy < len(maps):
                    if visited_map[yy][xx] == 0 and maps[yy][xx] != "X":
                        visited_map[yy][xx] = 1
                        que.append((yy, xx, cnt + 1))

    def find_E(y, x):
        que = deque()
        que.append((y, x, 0))
        while que:
            y, x, cnt = que.popleft()
            if maps[y][x] == "E":
                return cnt
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < len(maps[0]) and 0 <= yy < len(maps):
                    if visited_map[yy][xx] == 0 and maps[yy][xx] != "X":
                        visited_map[yy][xx] = 1
                        que.append((yy, xx, cnt + 1))

    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited_map = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    lever_map = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                a = find_L(i, j)
                # print(len(a))
                if a is None:
                    answer = -1
                    return answer
                else:
                    answer = a[2]
                    # print(a)
                    # # print(answer)
                    visited_map = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
                    b = find_E(a[0], a[1])
                    if b is None:
                        answer = -1
                        return answer
                    else:
                        # print(b)
                        answer = answer + b

    return answer



