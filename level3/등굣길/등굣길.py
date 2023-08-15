def solution(m, n, puddles):
    answer = 0
    mapp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(len(puddles)):
        mapp[puddles[i][1] - 1][puddles[i][0] - 1] = "@"
    # print(mapp)
    mapp[0][0] = 1

    for j in range(m):
        if mapp[0][j] != "@":
            mapp[0][j] = 1
        elif mapp[0][j] == "@":
            for i in range(j + 1, m):
                mapp[0][i] = "@"
            break
    for i in range(n):
        if mapp[i][0] != "@":
            mapp[i][0] = 1
        elif mapp[i][0] == "@":
            for j in range(i + 1, n):
                mapp[j][0] = "@"
            break

    for i in range(1, n):
        for j in range(1, m):
            if mapp[i][j] != "@":
                if j != 0 and mapp[i][j - 1] != "@":
                    mapp[i][j] = mapp[i][j - 1] % 1000000007 + mapp[i][j] % 1000000007
                if i != 0 and mapp[i - 1][j] != "@":
                    mapp[i][j] = mapp[i - 1][j] % 1000000007 + mapp[i][j] % 1000000007
    answer = mapp[-1][-1] % 1000000007

    return answer
