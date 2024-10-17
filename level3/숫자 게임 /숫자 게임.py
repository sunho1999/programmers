def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    idx_a = 0
    idx_b = 0

    for i in range(len(A)):
        if B[idx_b] > A[idx_a]:
            idx_a += 1
            idx_b += 1
            answer += 1
        else:
            B.pop()
            idx_a += 1

    return answer