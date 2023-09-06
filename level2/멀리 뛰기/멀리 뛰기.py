def solution(n):
    answer = 0
    dp = [1 for _ in range(n+3)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    if n == 1:
        answer = 1
    elif n ==2:
        answer = 2
    elif n==3:
        answer = 3
    if n >=4:
        for i in range(4,n+3):
            dp[i] = (dp[i-1]% 1234567 + dp[i-2]% 1234567)% 1234567
    answer = dp[n] % 1234567
    return answer