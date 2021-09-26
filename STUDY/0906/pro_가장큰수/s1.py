def solution(numbers):
    tmp=[]
    for index, num in enumerate(numbers):
        # 두자리수 세자리수 네자리수에 관계없이 맨 앞자리를 봐야하기 때문
        if num < 10:
            num = num*1111
        elif num<100:
            num=num*101
        elif num<1000:
            num=num*10+(num//100)
        tmp.append([num,index])

    # 정렬 후에 반대로 전환
    tmp.sort()
    tmp.reverse()

    answer=[]
    for i in range(len(numbers)):
        # tmp에 있는 인덱스에 맞춰서 리스트에 append
        answer.append(str(numbers[tmp[i][1]]))
    answer=''.join(answer)
    answer=int(answer)
    return str(answer)

print(solution([6, 10, 2]))