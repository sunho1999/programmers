def solution(n):
    answer = ''
    dp = [1, 2, 4]
    string = ""
    if n <= 3:
        answer = str(dp[n - 1])
    else:

        while n > 0:
            n = n - 1
            answer = str(dp[n % 3]) + answer
            n = n // 3
    return answer