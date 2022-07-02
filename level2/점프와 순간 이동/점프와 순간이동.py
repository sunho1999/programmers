def solution(n):
    ans = 0

    while (n != 1):
        if n == 2:
            break
        elif n % 2 == 0:  # 2로 나눠질 때
            n = n // 2
        else:  # 2로 안나눠질 때
            n = n // 2
            ans += 1

    ans += 1
    return ans