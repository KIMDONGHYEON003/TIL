import sys
sys.stdin = open("input.txt")

for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = list(map(int, input().split()))

    if y1 < y3 < y2 and x1 < x3 < x2:
        result = 'a'
    elif x3 < x1 < x2 < x4 or y1 < y3 < y4 < y2:
        result = 'a'
    elif x1 < x3 < x4 < x2 or y3 < y1 < y2 < y4:
        result = 'a'

    elif x2 == x3 and y1< y3 < y2:
        result = 'b'
    elif y2 == y3 and x1 < x3 < x2:
        result = 'b'

    elif x2 == x3 and y2 == y3:
        result = 'c'
    else:
        result = 'd'

    print(result)