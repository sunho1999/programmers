def solution(m, n, board):
    answer = 0
    check = []
    new_board = []

    for i in board:
        a = list(i.strip())
        new_board.append(a)  # 보드 배열화
    while True:
        check = []
        for i in range(m - 1):  # y
            for j in range(n - 1):  # x
                if new_board[i][j] == "0":  # 탐색한 좌표가 0일시 패스
                    continue

                if new_board[i][j] == new_board[i][j + 1]:
                    if new_board[i][j] == new_board[i + 1][j] and new_board[i][j + 1] == new_board[i + 1][
                        j + 1]:  # x,y좌표 2*2 탐색했을 때 전부 같은 값일 때
                        check.append((i, j))
                        check.append((i, j + 1))
                        check.append((i + 1, j))
                        check.append((i + 1, j + 1))
        if len(check) == 0:
            break
        else:
            answer += len(set(check))

            for c in check:
                new_board[c[0]][c[1]] = "0"  # 터질 블록들 0으로 초기화

            for c in reversed(check):  # 블록들 내리기 (밑에 있는 좌표부터 탐색할수 있도록 reversed로 뒤집음)
                check_n = c[0] - 1  # 터진 좌표로부터 하나하나씩 값을 바꿀 좌표
                put_n = c[0]  # 터진좌표를 저장할 값

                while check_n >= 0:  # 터진 자리 위에 있는 블록들을 다 내린다.
                    if new_board[put_n][c[1]] == "0" and new_board[check_n][c[1]] != "0":
                        new_board[put_n][c[1]] = new_board[check_n][c[1]]
                        new_board[check_n][c[1]] = "0"
                        put_n -= 1

                    check_n -= 1

    return answer