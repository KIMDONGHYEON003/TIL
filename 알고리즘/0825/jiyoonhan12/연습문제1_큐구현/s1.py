"""
문제1-1. 기본 Queue 구현 - 기본 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

#1. Queue 생성 (리스트)
Q = []

#2. Queue에 데이터를 삽입
Q.append(1)
Q.append(2)
Q.append(3)
print(Q)

#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
print(Q.pop(0))
print(Q)
print(Q.pop(0))
print(Q)
print(Q.pop(0))
print(Q)


print('-------------------------')

"""
문제1-2. 기본 Queue 구현 - 기본 구현 (내장 모듈 활용)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

from collections import deque

#1. Queue 생성
Q2 = deque([])

#2. Queue에 데이터를 삽입
Q2.append(2)
Q2.append(3)
Q2.appendleft(1) # appendleft 가능!
print(Q2)

#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
print(Q2.popleft())
print(Q2)
print(Q2.popleft())
print(Q2)
print(Q2.popleft())
print(Q2)