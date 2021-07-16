# 20차시_연습문제1.py

score = [88,30,61,55,95]
for i in range(1,6):
    if score[i-1] >= 60:
        result = "합격"
    else:
        result="불합격"

    print("%d번 학생은 %d점으로 %s입니다."% (i, score[i-1], result))