from collections import deque


def solution(cacheSize, cities):
    answer = 0
    que = deque()

    # 리스트의 각 요소를 소문자로 변환하여 새로운 리스트 생성
    cities = [word.lower() for word in cities]

    for i in cities:
        if len(que) < cacheSize:
            if i in que:  # cache hit
                # 특정 원소의 인덱스를 구함
                que.remove(i)
                que.append(i)
                answer += 1
            elif i not in que:
                que.append(i)
                answer += 5  # cache miss
        elif len(que) == cacheSize:  # 다 찼을 때
            if i in que:  # cache hit
                # 특정 원소의 인덱스를 구함
                que.remove(i)
                que.append(i)
                answer += 1
            elif i not in que:
                que.append(i)
                que.popleft()
                answer += 5  # cache miss
    return answer