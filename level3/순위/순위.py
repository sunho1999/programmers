def solution(n, results):
    wins, loses = {}, {}

    for i in range(1, n + 1):
        wins[i], loses[i] = set(), set()
    for i in range(1, n + 1):
        for r in results:
            if r[0] == i:
                wins[i].add(r[1])
            if r[1] == i:
                loses[i].add(r[0])
        for winner in loses[i]:
            wins[winner].update(wins[i])

        for loser in wins[i]:
            loses[loser].update(loses[i])

    cnt = 0
    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            cnt += 1

    return cnt