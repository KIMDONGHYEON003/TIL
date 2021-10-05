import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    password = list(map(str, input()))
    cnt = N // 4
    arr = []
    for i in range(cnt): # cnt 만큼 회전해야함
        pop_num = password.pop()    # 리스트 끝을 맨 앞으로 옮긴다.
        password.insert(0, pop_num)

        for j in range(0, N, cnt): # 리스트 내에서 각각 떨어져있는 요소를 하나의 번호로 합침
            number = ''
            for k in range(j, j+cnt):
                number += password[k]
            arr.append(number)

    arr = set(arr)   # 중복 제거
    demi = []
    for num in arr:
        demi.append(int(num, 16))  # 10진수로 변환
        
    result = sorted(demi, reverse=True) #내림차순 정렬
    print('#{} {}'.format(t+1, result[K-1]))