# 20차시_연습문제10_숫자개수
# 다음의 결과와 같이 어떤 한 양의 정수를 입력하여
#  그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

array = [0]*10
num = int(input())
result = ""

while num:
    array[num%10]+=1
    num//=10

for i in range(0,10):
    result += "%d" % i
print(result[0:len(result)-1])

result = ""

for i in range(0,10):
    result +="%d" % array[i]
print(result[0:len(result)-1])