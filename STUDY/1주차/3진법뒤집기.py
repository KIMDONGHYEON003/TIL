def solution(n):
    answer = 0
    tmp_list = []
    n = int(input())

    while True:
        if n == 0:
            return tmp_list
            
        else:
            n = n // 3
            tmp_list.append(n%3)
        break
print(solution(45))
        

    