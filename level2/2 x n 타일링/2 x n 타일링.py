def solution(n):
    answer = 0
    max_num = 1000000007
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    if n ==1:
        answer = 1
    elif n ==2:
        answer = 2
    elif n >=3:
        for i in range(3,n+1):
            dp[i] = dp[i-1]%max_num + dp[i-2]%max_num
    # print(dp)
    answer = dp[n]%max_num
    return answer