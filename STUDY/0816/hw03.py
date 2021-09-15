def solution(string):
    result = []
    for n in range(len(string)):
        new_string = ['' for _ in range(len(string))]
        for i in range(len(string)):
            k = i - n
            new_string[i] = string[k]

        stack = []
        for s in new_string:
            if s == '{' or s == '(' or s == '[':
                stack.append(s)
            elif s == '}':
                if len(stack) and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(s)
            elif s == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
            elif s == ']':
                if len(stack) and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s)

        result.append(len(stack))
    return result.count(0)

string = '(){}[]'
print(solution(string))
