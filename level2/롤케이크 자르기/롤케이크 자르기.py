from collections import Counter

def solution(topping):
    answer = 0
    bro = Counter(topping)
    chulsoo = set()
    for i in topping:
        bro[i] -=1
        if bro[i] == 0:
            del bro[i]
        chulsoo.add(i)
        if len(bro) == len(chulsoo):
            answer +=1
    return answer