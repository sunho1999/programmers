def solution(n):
    answer = 0
    if n == 1:
        answer = 1
    else:
        if n % 2 == 0:  # 짝수일 때
            div = n // 2
            dp = [i for i in range(1, div + 1)]
        elif n % 2 == 1:  # 홀수일 때
            div = n // 2 + 1
            dp = [i for i in range(1, div + 1)]

        for i in range(1, div):
            dp[i] = dp[i] + dp[i - 1]

        if n in dp:
            answer += 1
        for i in range(len(dp) - 1):
            for j in range(i + 1, len(dp)):
                if dp[j] - dp[i] == n:
                    answer += 1
                if dp[j] - dp[i] > n:  # 시간초과 해결 코드
                    break
        answer += 1
    return answer