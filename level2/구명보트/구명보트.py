def solution(people, limit):
    answer = 0
    right = len(people) - 1  # 제일 우측 idx
    left = 0  # 제일 왼쪽 idx
    people = sorted(people, reverse=False)  # 정렬

    while (left <= right):
        answer += 1
        if people[left] + people[right] <= limit:  # 2명 탈수 있을 때
            left += 1
            right -= 1
        elif people[left] + people[right] > limit:  # 기본 단계
            right -= 1

    return answer