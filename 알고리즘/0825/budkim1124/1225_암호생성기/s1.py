from collections import deque
import sys
sys.stdin = open("input.txt")

for _ in range(10):
    num = int(input())
    q_list = list(map(int, input().split()))
    Q = []
    cnt = 1

    while True:
        Q = q_list.pop(0)
        Q -= cnt
        cnt += 1
        if cnt == 6:
            cnt = 1
        if Q <= 0:
            Q = 0
            break
        q_list.append(Q)

    result = ' '.join(map(str, q_list))
    print("#{} {} 0".format(num, result))
