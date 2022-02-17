from collections import deque

def solution(number, k):
    answer = deque()  # answer 구할 리스트
    text = ''

    for i in number:
        if len(answer) == 0:
            answer.append(i)
        else:
            while (answer and i > answer[-1] and k != 0):
                answer.pop()
                k -= 1
            answer.append(i)
    for i in answer:
        text += i
    if k != 0:  # k 나머지 값 정리하기
        text = text[0:len(text) - k]

    return text