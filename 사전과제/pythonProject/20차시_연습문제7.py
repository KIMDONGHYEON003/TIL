# 20차시_연습문제7.py

score = [85,65,77,83,75,22,98,88,38,100]
result=0

while len(score):
    k= score.pop()
    if k >= 80:
        result +=k

print(result)
