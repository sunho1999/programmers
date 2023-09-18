def solution(n, words):
    start_word = [words[0][0]]
    for i, w in enumerate(words):
        if w not in start_word and start_word[-1][-1] == w[0]:
            start_word.append(w)
        else:
            return [i%n+1, (i//n)+1]
    return [0, 0]