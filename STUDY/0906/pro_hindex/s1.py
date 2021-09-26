def solution(citations):
    citations.sort()
    answer = 0
    h = 0
    k = 0
    for i in range(0, citations[-1]+1):
        for j in citations:
            if j >= i:
                h += j
            if j <= i:
                k += j
        if h >= i and k <= i:
            if i > answer:
                answer = i
    if citations[0] >= len(citations):
        answer = len(citations)
    return answer

print(solution([3, 0, 6, 1, 5]))