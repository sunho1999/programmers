def solution(genres, plays):
    answer = []
    unique_genres = list(set(genres))
    music_cnt = {}
    music_idx = {}
    for i in range(len(genres)):
        if genres[i] not in music_cnt:
            music_cnt[genres[i]] = 0  # 노래 카운트
            music_cnt[genres[i]] += plays[i]

            music_idx[genres[i]] = []
            music_idx[genres[i]].append((str(i), plays[i]))
        else:
            music_cnt[genres[i]] += plays[i]
            music_idx[genres[i]].append((str(i), plays[i]))

    music_cnt = sorted(music_cnt.items(), key=lambda x: x[1], reverse=True)
    # print(music_cnt)
    # 튜플의 두 번째 원소를 기준으로 리스트 정렬
    for i in music_idx:
        music_idx[i] = sorted(music_idx[i], key=lambda x: x[1], reverse=True)
    for i, j in music_cnt:
        if len(music_idx[i]) == 1:
            answer.append(int(music_idx[i][0][0]))
        else:
            for k in range(len(music_idx[i]) // 2):
                answer.append(int(music_idx[i][k * 2][0]))
                answer.append(int(music_idx[i][k * 2 + 1][0]))
                break
                # answer.append(music_idx[k*2+1][0])
    return answer