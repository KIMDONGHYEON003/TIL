# 함수연습문제_카운트다운.py

def countdown(k):
    if k <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    for i in range(k, 0, -1):
        print(i)


countdown(0)
countdown(10)