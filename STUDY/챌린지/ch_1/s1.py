def solution(numbers):
    numbers = sorted(numbers)
    num_lst = [0] * 10
    result = 0

    for i in range(len(num_lst)):
        for num in numbers:
            if i == num:
                num_lst[i] += num

    for k in range(len(num_lst)):
        if num_lst[k] == 0:
            result += k

    return result



print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))