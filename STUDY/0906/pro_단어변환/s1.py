def solution(begin, target, words):
    answer = []

    # 리스트에 target이 없이면 아예 불가능
    if target not in words:
        return 0

    # 한 자만 다르면 True, 아니면 False
    def check(begin, tmp_word):
        cnt = 0
        for a, b in zip(begin, tmp_word):
            if a != b:
                cnt += 1
        return cnt == 1

    def search(target, words, change):
        for word in words:
            # check 함수 사용해서 한자만 다른지 확인 / 같으면 일단 리스트에 저장
            if word == target and check(begin, word):
                # change를 추가해서 나중에 최단거리를 구하기 위함
                answer.append(change)
            # 아직 target에 도달하지 못했을 때
            elif check(target, word):
                words.remove(target)
                # target을 현재 word로 바꾼다
                search(word, words, change + 1)

    search(target, words, 1)

    # answer의 값 중 최솟값을 반환
    return min(answer)

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))