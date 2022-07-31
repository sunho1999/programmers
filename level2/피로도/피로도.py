import itertools


def solution(k, dungeons):
    que = []
    que = itertools.permutations(dungeons, len(dungeons))
    que = list(que)
    total_answer = []
    for i in que:
        answer = 0
        pirodo = k
        for j in i:
            if j[0] <= pirodo:
                pirodo = pirodo - j[1]
                answer += 1
            elif j[0] > pirodo:
                pass
        total_answer.append(answer)
    m = max(total_answer)
    return m