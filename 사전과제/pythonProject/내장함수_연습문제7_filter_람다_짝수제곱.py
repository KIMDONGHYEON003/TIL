# 내장함수_연습문제7_filter_람다_짝수제곱.py

lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result1 = list(filter(lambda x: not (x & 1) , lit))
result2 = list(map(lambda x: x**2 , result1))

print(result2)