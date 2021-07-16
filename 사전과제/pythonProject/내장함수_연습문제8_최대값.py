# 내장함수_연습문제8_최대값.py

def maxCheck(*param):
    print("max{0} => {1}".format(param, max(param)))


maxCheck(3, 5, 4, 1, 8, 10, 2)