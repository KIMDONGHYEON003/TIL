def solution(i, my_sum, numbers, target):
    global cnt

    if len(numbers) == i:
        if my_sum == target:
            cnt += 1
        return
    else:
        # del numbers[0]

        solution(i+1, my_sum + numbers[i], numbers, target)
        solution(i+1, my_sum - numbers[i], numbers, target)

def finish(numbers, target):

    solution(0, 0, numbers, target)

    return cnt

cnt = 0
print(finish([1,1,1,1,1], 3))