# 20차시_연습문제6.py

blood = ['A','A','A','O','B','B','O','AB','AB','O']

count_a=0
count_b=0
count_o=0
count_ab=0


for i in range(0,10) :
    if blood[i] == 'A':
        count_a +=1
    elif blood[i] =='B':
        count_b += 1
    elif blood[i] == 'O':
        count_o +=1
    else:
        count_ab += 1


print("{'A': %d, 'O' : %d, 'B' : %d, 'AB' : %d}" %(count_a, count_o, count_b, count_ab))