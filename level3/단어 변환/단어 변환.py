from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    que = deque()
    que.append((begin, 0))

    while que:
        check_list = [False for _ in range(len(words))]  # 방문개수 체크
        a, idx = que.popleft()
        if a == target:
            break

        for word in words:
            cnt = 0
            for j in range(len(word)):
                if a[j] == word[j]:
                    cnt += 1
            check_list[words.index(word)] = cnt

        for i in range(len(check_list)):
            if check_list[i] == (len(target) - 1):
                que.append((words[i], idx + 1))
                words[i] = str(idx)
    return idx