# 후위표기법으로 변경..
def change(Arr):
    Stack = []
    Count = []
    for i in range(len(ARR)):
        # 숫자일 때 그냥 append
        if ARR[i].isdigit():
            Count.append(ARR[i])
            continue
        # 괄호가 있는지 체크하고 추가..
        if ARR[i] == '(':
            Stack.append(ARR[i])
            continue
        # 더하기 일때..
        elif ARR[i] == '+':
            while Stack:
                if Stack[-1] == '(': break
                Count.append(Stack.pop())
            Stack.append(ARR[i])
            continue
        elif Arr[i] =='*':
            while Stack[-1] =='*':
                Count.append(Stack.pop())
            Stack.append(ARR[i])
            continue
        elif ARR[i] == ')':
            while Stack:
                if Stack[-1] == '(':
                    Stack.pop()
                    break
                Count.append(Stack.pop())
    return Count
# 후위표기법 계산..
def cal(lst):
    Stack = []
    for i in range(len(lst)):
        # 숫자면 stack에 저장..
        if lst[i].isdigit():
            Stack.append(lst[i])
        # 문자일때 연산후 Stack에 다시 저장..
        else:
            a = int(Stack.pop())
            b = int(Stack.pop())
            if lst[i] == '+': Stack.append(a+b)
            elif lst[i] == '*': Stack.append(b*a)
    return Stack

T = 10

for tc in range(1, T+1):
    N = int(input())
    ARR = list(input())
    print('#{}'.format(tc), end=' ')
    print(*cal(change(ARR)))