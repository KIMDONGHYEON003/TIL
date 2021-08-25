import sys
sys.stdin = open('input.txt')

N = int(input())
data = input()
stack = []
result = []

#1. 중위 표현식 -> 후위 표현식
for i in range(N):

    if data[i] == '*':          # 곱셈인 경우
        while stack and stack[-1] == '*':   # 스택이 존재하고, 가장 최근에 넣은 것이 *
            result.append(stack.pop())
        stack.append(data[i])

    elif data[i] == '+':        # 덧셈인 경우
        while stack:            # 스택이 있으면
            result.append(stack.pop())
        stack.append(data[i])
    else:
        result.append(data[i])

while stack:
    result.append(stack.pop())

ans = "".join(result)
print(ans)

#2. 후위 표현식 -> 계산

# data
#
# for char in data:
#     if char == '*':
#
#     elif char == '+':
#
#     else: