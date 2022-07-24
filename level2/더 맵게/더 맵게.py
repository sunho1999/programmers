import heapq
import sys
sys.setrecursionlimit(100000)
def check(scoville,K): # 모든 음식이 스코빌 지수가 넘는지 확인

    for i in scoville:
        if i < K:
            return True
    return False

def solution(scoville, K):
    answer = 0
    is_check = True
    heapq.heapify(scoville)
    while(is_check):
        if len(scoville) == 2:  # 개수가 2이상부터 시작인데 2개일땐 1,2 원소를 뺴면 1개밖에 안남으므로 이때 예외처리하여 조건 탐색
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            item = first + second*2
            heapq.heappush(scoville,item)
            is_check = check(scoville,K)
            if is_check == False: # 2개 남았을 때 2개를 조합하여 새로운 음식을 만들었는데 스코빌 지수가 넘었을 때
                answer +=1
                break
            else: # 조합한 새로운 음식이 스코빌 지수를 넘지 못했을 때
                answer = -1
                break
        else: # 스코빌 지수 공식대로 진행
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            if first >= K and second >= K:
                heapq.heappush(scoville,first)
                heapq.heappush(scoville,second)
                is_check = check(scoville,K)
            else:
                item = first + second*2
                heapq.heappush(scoville,item)
                is_check = check(scoville,K)
                answer +=1
    return answer