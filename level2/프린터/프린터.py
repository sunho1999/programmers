from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque()
    idx_list = [i for i in range(len(priorities))]
    for i in range(len(priorities)):
        que.append((priorities[i],idx_list[i]))
    while que:
        num,idx = que.popleft()
        if que and max(que)[0] > num:
            que.append((num,idx))
        else:
            answer += 1
            if idx == location:
                break
    return answer