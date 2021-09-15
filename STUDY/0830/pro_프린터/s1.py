def solution(priorities, location):
    answer = 0
    priorities = [(data, idx) for idx, data in enumerate(priorities)]

    while len(priorities) != 0:
        item = priorities.pop(0)

        if priorities and max(priorities)[0] > item[0]:  
            priorities.append(item)     # 작으면 뒤로 순번을 미룸
        else:
            answer += 1     # 출력이 하나 될 때마다 1씩 더해줌
            if item[1] == location:     # location의 위치와 같으면 break
                break

    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))