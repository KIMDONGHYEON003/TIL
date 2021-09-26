def solution(numbers):
    answer = ''
    tmp = []
    for i, num in enumerate(numbers):
        tmp.append([str(num) * 4, i])
    tmp.sort(reverse=True)
    for i in tmp:
        answer += str(numbers[i[1]])

    return answer


print(solution([6, 10, 2]))