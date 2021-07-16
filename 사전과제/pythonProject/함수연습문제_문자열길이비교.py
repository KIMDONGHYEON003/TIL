# 함수연습문제_문자열길이비교.py
def length(k):
    if k[0] > k[1]:
        print(k[0])
    else:
        print(k[1])


k = input()
k = k.split(', ')
length(k)
