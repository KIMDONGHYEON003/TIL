import sys
sys.stdin = open("input.txt")

height = []
for _ in range(9):
    h = int(input())
    height.append(h)
result2 = []

for i in range(1, 1 << len(height)):
    result1 = []
    for j in range(len(height)):
        if i & (1 << j):
            result1.append(height[j])
    result2.append(result1)

for nums in result2:
    if len(nums) == 7 and sum(nums) == 100:
        for num in sorted(nums):
            print(num)
        break                   # 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.