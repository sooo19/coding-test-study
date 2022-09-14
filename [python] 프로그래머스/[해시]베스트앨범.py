def solution(genres, plays):
    answer = []

    total = {}      # 장르 별 총 재생 횟수
    gen_dic = {}    # 장르별 [재생횟수, 고유번호] 배열을 value로 가지는 딕셔너리

    # total 딕셔너리 생성
    for i in range(len(genres)):
        if genres[i] not in total:      # 딕셔너리에 해당 음악 종류가 없는 경우 새로 추가
            total[genres[i]] = plays[i]
            gen_dic[genres[i]] = [(plays[i], i)]
        else:       # 딕셔너리에 해당 음악 종류가 있는 경우, 그대로 새로운 정보를 append 또는 값을 더함
            total[genres[i]] += plays[i]
            gen_dic[genres[i]].append((plays[i], i))

    # print(total)
    # print(gen_dic)

    # total 딕셔너리 정렬 (조회 수 기준으로)
    total = sorted(total.items(), key = lambda x : x[1], reverse = True)
    # print(total)

    # 전체 조회수 순으로 정렬된 total 배열의 key를 활용해서 각 장르의 [조회수, 고유번호] 정보를 배열로 저장함
    # 전체 조회수가 높은 -> 낮은 순으로 playlist 배열에 값이 저장됨
    for key in total:
        playlist = gen_dic[key[0]]      # 딕셔너리의 value 값인 [조회수, 고유번호] 배열을 모두 가져와 저장
        # 조회수 순으로 [조회수, 고유번호] 배열을 정렬
        playlist = sorted(playlist, key = lambda x: x[0], reverse = True) 
        for i in range(len(playlist)):      
            if i < 2:
                answer.append(playlist[i][-1])
            else:
                break
        # for 문이 한 번 돌 때마다, playlist 배열에는 한 장르의 (재생수, 고유번호) 정보가 재생 수를 기준으로 내림차순 정렬됨
        # 정렬된 playlist 배열을 앞에서부터 두 개씩 answer 배열에 저장 (두 개 넘어가면 break를 통해 다음 장르로 넘어가도록 설정)

    # print(playlist)    
    return answer

ans = solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
print(ans)