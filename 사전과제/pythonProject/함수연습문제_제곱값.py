# 함수연습문제_제곱값.py

def square(k):
    print("square(%d) => %d" % (int(k), int(k) ** 2))


k = input()
k = k.split(', ')
for i in k:
    square(i)

