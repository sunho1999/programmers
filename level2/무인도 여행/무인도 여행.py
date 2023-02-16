from collections import deque
import sys

global sum_list
global visit_list

sys.setrecursionlimit(10000)
que = deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
matrix = []
total_sum = 0


def dfs(i, j, visit_list, sum_list):
    global total_sum

    if visit_list[i][j] == 0:
        total_sum = int(matrix[i][j])
        visit_list[i][j] = 1

    for k in range(4):
        idx_i = dx[k] + i
        idx_j = dy[k] + j
        if 0 <= idx_i < len(matrix) and 0 <= idx_j < len(matrix[0]):
            if (matrix[idx_i][idx_j] in num_list) and visit_list[idx_i][idx_j] == 0:
                total_sum += dfs(idx_i, idx_j, visit_list, sum_list)
                visit_list[idx_i][idx_j] == 1
    return total_sum


def solution(maps):
    answer = []
    for i in maps:
        matrix.append(list(i))
    sum_list = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    visit_list = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    a = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] in num_list:
                if visit_list[i][j] == 0:
                    que.append((i, j))
                    a = dfs(i, j, visit_list, sum_list)
                    answer.append(a)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort(reverse=False)
    return answer