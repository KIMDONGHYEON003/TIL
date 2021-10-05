def solution(n, lost, reserve):
    # 그냥 수업을 들을 수 있는 학생 수
    answer = n - len(lost)
    # 앞 뒤로만 빌려줄 수 있기 때문에 정렬
    lost.sort()
    reserve.sort()
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수(제한사항)
    lost_reserve = set(lost) & set(reserve)
    answer += len(lost_reserve)

    # 리스트에 이미 추가했기 때문에 제거해준다
    for lr in lost_reserve:
        lost.remove(lr)
        reserve.remove(lr)

    # 도난당한 학생들 중에서
    for s_lost in lost:

        # 앞번호
        if (s_lost-1) in reserve:
            reserve.remove(s_lost-1)
            answer += 1

        # 뒷번호
        elif (s_lost+1) in reserve:
            reserve.remove(s_lost+1)
            answer += 1

    return answer

print(solution(5,[2, 4]	,[1, 3, 5]	))