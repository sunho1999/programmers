from collections import Counter

def solution(gems):
    num = len(set(gems))
    ret = []
    left = 0
    counter = Counter()
    for right in range(len(gems)):
        counter[gems[right]] += 1
        right += 1
        while len(counter) == num: # 탐색을 했을 때 주어진 보석 리스트를 전부 찾았을 때
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0: # 이후 중복된 원소가 더 없다는 걸 의미
                del counter[gems[left]] # 이러면서 while 조건문 빠져나옴
            left += 1
            ret.append([left, right])
    return sorted(ret, key = lambda x: (x[1]-x[0], x[0]))[0]