def solution(A, B):
    answer = 0

    A = sorted(A, reverse=True)
    B = sorted(B, reverse=False)
    print(A, B)
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer