def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+1):
        dp[i] =  (dp[i-1] + dp[i-2]) % 1234567
    answer = dp[n]% 1234567
    return answer