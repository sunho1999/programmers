from collections import deque

def check(que, speeds):
    count = 0
    while que:
        if que[0] >= 100:
            que.popleft()
            speeds.popleft()
            count += 1
        else:
            return count
    return count


def solution(progresses, speeds):
    answer = []

    que = deque(progresses)
    speeds = deque(speeds)

    while que:
        for j in range(len(que)):
            que[j] += speeds[j]

        if que[0] >= 100:
            a = check(que, speeds)
            if a > 0:
                answer.append(a)
    return answer