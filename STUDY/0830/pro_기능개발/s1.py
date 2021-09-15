import sys
sys.stdin = open("input.txt")
from collections import deque
# 덱을 사용

def solution(progresses, speeds):
    answer = []                     # cnt가 들어갈 list
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        cnt = 0

        for i in range(len(progresses)):
            if progresses[i] >= 100:    # 100이상이면 그냥 아무것도 안함
                continue
            else:
                progresses[i] = progresses[i] + speeds[i]   # 100보다 작으면 speed를 하나씩 더해줌

        while progresses[0] >= 100: # 앞쪽부터 배포해야하기 때문에 index 0 값으로 함
            progresses.popleft()
            speeds.popleft()
            cnt += 1

            if len(progresses) == 0:
                break

        if cnt > 0:
            answer.append(cnt)
    return answer

T = int(input())

for t in range(T):
    progresses = list(map(int, input().split()))
    speeds = list(map(int, input().split()))

    print(solution(progresses, speeds))