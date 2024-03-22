import math
def solution(arrayA,arrayB):
    answer = 0
    gc,vc= 0,0

    for i in range(len(arrayA)):
        gc = math.gcd(gc,arrayA[i])

    for i in range(len(arrayB)):
        vc = math.gcd(vc,arrayB[i])

    for j in range(len(arrayA)):
        if arrayA[j] % vc == 0:
            vc = 1
        if arrayB[j] % gc == 0:
            gc = 1

    if gc == 1 and vc ==1:
        return 0
    else:
        return max(gc,vc)