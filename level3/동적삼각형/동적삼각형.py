def solution(triangle):
    answer = 0
    dp = []
    for i in range(1,len(triangle)+1):
        dp.append([0 for j in range(i)])
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[1][0] + triangle[0][0]
    dp[1][1] = triangle[1][1] + triangle[0][0]
    for i in range(2,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(triangle[i][j] + dp[i-1][j-1],triangle[i][j] + dp[i-1][j])
    answer = max(dp[-1])
    return answer

