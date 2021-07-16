# 함수연습문제_팩토리얼.py

def factorial(i):
    result = 1
    for i in range(2, i+1):
        result = result * i
    return result

k = int(input())
print(factorial(k))