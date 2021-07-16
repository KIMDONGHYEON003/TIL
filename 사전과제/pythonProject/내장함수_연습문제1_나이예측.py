# 내장함수_연습문제1_나이예측.py
import datetime
name = input()
age = int(input())

t = int(100-age)
year = datetime.datetime.now().year-2+t

print("%s(은)는 %d년에 100세가 될 것입니다." %(name, year))