def solution(word):
    answer = 0
    char = ["A", "E", "I", "O", "U"]
    li = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += (char.index(word[i])) * li[i]
    answer += len(word)
    return answer