# 내장함수_연습문제5_filter_람다.py

lit = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: not (x & 1) , lit))
print(result)