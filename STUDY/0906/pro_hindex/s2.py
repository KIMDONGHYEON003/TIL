def solution(citations):
    citations.sort(reverse=True)
    # citations.reverse()
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)

print(solution([3, 0, 6, 1, 5]))