import numpy as np


def solution(arr1, arr2):
    answer = []

    arr1 = np.array(arr1)
    # print(arr1)
    arr2 = np.array(arr2)
    # print(arr2)
    a = np.dot(arr1, arr2)
    a = a.tolist()
    for i in a:
        answer.append(i)

    return answer