from collections import deque

# [[0,0,1,0],
#  [0,0,0,0],
#  [0,1,0,1],
#  [1,0,0,0]]
max_num = 1000000000


def solution(board):
    answer = []
    matrix = [[max_num for _ in range(len(board))] for _ in range(len(board))]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    direct = [0, 2, 1, 3]

    # 0 오른쪽
    # 1 아랫쪽
    # 2 왼쪽
    # 3 위쪽
    def bfs(x, y, cost, dirr):

        if dirr == 0:  # 오른쪽 출발
            que = deque()
            que.append((x, y, cost, dirr))
            while que:
                x, y, cost, dirr = que.popleft()
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    now_dir = direct[i]
                    if 0 <= xx < len(board) and 0 <= yy < len(board):
                        if dirr == now_dir:  # 같은 방향일 때
                            # print(y,x,dirr,now_dir)
                            new_cost = cost + 100
                        else:
                            new_cost = cost + 600
                        if board[yy][xx] == 0:  # 보드가 벽이 아닐때
                            if matrix[yy][xx] > new_cost:
                                matrix[yy][xx] = min(matrix[yy][xx], new_cost)
                                que.append((xx, yy, new_cost, now_dir))

        elif dirr == 1:  # 아랫쪽 출발
            que = deque()
            que.append((x, y, cost, dirr))
            while que:
                x, y, cost, dirr = que.popleft()
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    now_dir = direct[i]
                    if 0 <= xx < len(board) and 0 <= yy < len(board):
                        if dirr == now_dir:  # 같은 방향일 때
                            new_cost = cost + 100
                        else:
                            new_cost = cost + 600
                        if board[yy][xx] == 0:  # 보드가 벽이 아닐때
                            if matrix[yy][xx] > new_cost:
                                matrix[yy][xx] = min(matrix[yy][xx], new_cost)
                                que.append((xx, yy, new_cost, now_dir))
        # print(matrix)
        return

    answer = []
    # 오른쪽 방향
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                matrix[i][j] = 1
    matrix[0][0] = 0
    bfs(0, 0, 0, 0)
    answer.append(matrix[-1][-1])

    # 왼쪽 방향
    matrix = [[max_num for _ in range(len(board))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                matrix[i][j] = 1
    bfs(0, 0, 0, 1)
    answer.append(matrix[-1][-1])

    print(answer)
    return min(answer)