def solution(left, right):
    answer = 0
    factor = []
    result = []
    for num in range(left, right+1):
        factor = []
        for i in range(1, num+1):
            if num % i == 0:
                factor.append(i)
        cnt = len(factor)

        if cnt % 2 == 1:
            num = num * (-1)
            result.append(num)
        else:
            result.append(num)

    answer += sum(result)

    return answer

print(solution(13, 17))