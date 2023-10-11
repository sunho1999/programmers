def solution(n, left, right):
    answer = []
    for i in range(int(left),int(right)+1):
        a = i//n # 몫
        b = i%n #나머지
        c = max(a,b)
        answer.append(c+1)

    return answer