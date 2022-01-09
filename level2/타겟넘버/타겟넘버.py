from collections import deque


def solution(numbers, target):
    answer = 0
    que = deque()
    que.append((numbers[0], 0))
    que.append((-1 * numbers[0], 0))
    len_numbers = len(numbers)

    while que:
        num, idx = que.popleft()
        idx += 1
        if idx < len_numbers:
            que.append((num + numbers[idx], idx))
            que.append((num - numbers[idx], idx))
        elif idx == len_numbers:
            if num == target:
                answer += 1
    return answer