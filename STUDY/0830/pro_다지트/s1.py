def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge_weight = 0
    bridge = [0] * bridge_length

    while len(truck_weights) > 0:
        cnt += 1
        end = bridge.pop(0) # end는 이미 다리를 통과한 트럭
        bridge_weight -= end    # 이미 다리르 통과했기 때문에 end만큼 빼준다.

        if truck_weights[0] + sum(bridge) > weight: # 무게를 견딜 수 있는지 없는지 확인하기 위해
            bridge.append(0)            # 결딜수 없다면 bridge에 0을 append한다.
        else:
            bridge.append(truck_weights.pop(0)) # 견딜 수 있으면 트럭 한 대 다리 위로

    # 다리에 남은 트럭을 빼준다.
    while len(bridge) > 0:
        cnt += 1
        bridge.pop(0)

    return cnt

import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(T):
    bridge_length = int(input())
    weight = int(input())
    truck_weights = list(map(int, input().split()))

    print(solution(bridge_length, weight, truck_weights))