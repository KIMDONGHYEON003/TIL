# Queue

- ***선형 큐 ***

- 큐의 특성

  - 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
    - 큐의 뒤에는 삽입만 가능하고 큐의 앞에서서는 삭제만 이루어지는 구조
  - 선입 선출 구조
    - 큐에 삽입한 순서대로 원소가 저장, 가장 먼저 저장된 원소는 가장 먼저 삭제된다.

  enQueue(item) : 삽입

  deQueue() : 제거 앞쪽부터 제거

  createQueue() : 큐생성

  isEmpty() : 공백 확인

  isFull() : 포화 확인

  Qpeek() : 큐의 앞쪽에서 원소 삭제없이 반환

  1. 공백 큐 생성 : createQueue() - 필요한 크기 만큼 비어있는 큐를 생성
  2. 원소 a 삽입 : enQueue(a)
  3. 원소 b 삽입 : enQueue(b)
  4. 원소 반환/ 삭제 : deQueue()
  5. 원소 c 삽입 : enQueue(c)
  6. 원소 반환/삭제 : deQueue()
  7. front가 점점 이동하면서 front 부터 삭제됨

```python
## 큐 삽입
def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = rear +1
        Q[rear] = item
```

```python
### 공백 상태 포화상태
def isEmpty():
    return front == rear

def Full():
    
```

```python
def Qpeek():
    if isEmpty():
        print()
    else:
        return Q[front+1]
```



```python
Q = [0]*10
front = -1
rear = -1

rear += 1
Q[rear] = 2

rear += 1
Q[rear] = 2

rear +=1
Q[rear] = 3

while front != rear:
    front +=1
    print(Q[front], end=" ")
    
listQ = []
listQ.append(1)
listQ.append(2)
listQ.append(3)
while listQ:
    print(listQ.pop(0), end=" ")
print()

```

```python
from collections import deque

# enqueue -> append
q = deque()
q.append(1)
q.append(2)
q.append(3)

#dequeue -> popleft
while q:
    print(q.popleft())
```





- 잘못된 포화상태 인식
  - 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고 rear=n-1인 상태 즉, 포화 상태로 인식하여 더 이상의 삽입을 수행하지 않게됨
  - 해결방안
    - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
    - 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐 ( 좋은 방법은 아님
  - 해결 방안 2
    - 1차원 배열을 사용하되, 논리적으로 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용



- 초기 공백 상태
  - front = rear = 0
- 인덱스의 순환
  - fornt와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야함
  - 이를 위해 나머지 연선자 mod를 사용





- 원형 큐

  - 초기 공백 큐 생성

    - 크기 n인 1차원배열 생성

  - 공백 상태 및 포화 상태 검사

    ```python
    def isEmpty():
        return front == rear
    
    def isFull():
        return (rear+1) % len(cQ) == front # 다음 칸이 front네
    ```

    



- 연결 큐의 구조

  - 단순 연결 리스트를 이용한 큐
    - 큐의 원소 : 단순 연결 리스트의 노드
    - 큐의 원소 순서 : 노드의 연결 순서 링크로 연결되어 있음
    - front : 첫번째 노드를 가리키는 링크
    - rear : 마지막 노드를 가리키는 링크
  - 상태표현
    - 초기 상태 : front = rear = null
    - 공백 상태 : front = rear = null

  - 연결 큐의 구현

  - ```python
    class Node:
        def __init__(self, item, n=None):
            self.item = item
            self.next = n
            
    def enQueue(item):	#연결 큐의 삽입 연산
        global front, rear
        newNode = Node(item)	# 새로운 노드의 생성
        if front == None:
            front = newNode
        else:
            rear.next = newNode
        rear = newNode
    ```





- 우선순위 큐
  - 특성
    - 우선 순위를 가진 항목들을 저장하는 큐
    - fifo 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다.
  - 적용분야
    - 시뮬 시스템
    - 네트워크 트래픽 제어
    - 운영체제의 테스크 스케쥴링





- 큐의 활용
  - 버퍼 : 임시 저장소
  - 버퍼의 자료구조
    - 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
    - fifo 방식인 큐가 사용됨





- BFS (너비우선탐색)

  - 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
  - 인접한 정접들에 대해 탐색을 한 후, 차례로 다시 너비 우선 탐색을 진행해야하므로, 선입 선출 형태의 자료구조의 큐를 활용함
  - 입력 파라미터 : 그래프 G와 탐색 시작점 v

  ```python
  def BFS(G, v): # 그래프 G, 탐색 시작점 V
  	visoted = [0] * (n+1)	#정점의 개수 n / 방문표시 배열 생성
      queue = []	# 큐 생성
      queue.append(v)	# 시작접 v를 큐에 삽입
      while queue:	# 큐가 비어있지 않은 경우
          t = queue.pop(0)	# 큐의 첫번째 원소 반환
          if not visitied[t]:	# 방문되지 않은 곳이라면
              visitied[t] = True	# 방문한 것으로 표시
              visit(t)			# 정점 t에서 할 일
              for i in G[t]:		#t 와 연결된 모든 정점에 대해
                  if not visited[i]:	# 방문되지 않은 곳이라면
                      queue.append(i)	# 큐에 넣기
          
  ```

  



```python
def bfs(s, V):
    q = [] 					# 큐 생성
    visited = [0] * (V+1) 	# visited 생성
    q.append(s)				# 시작점 인큐
    visited[s] = 1			# 시작점 visited 표시
    while q:				# 큐가 비어있지 않으면 ( 처리할 정점이 남아 있으면)
    	t = q.pop(0)		# 디큐 ( 꺼내서)해서 t에 저장
    	print(t)			# t에 대한 처리
    	for i in range(1, V+1):# t에 인접이고 미방문인 모든 i에
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i) # enqueue(i)
                visited[i] = visited[t] +1 	# i visited로 표시

V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) in range(V+1)]			# 인접행렬

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 ## 방향이 없는 그래프이기 때문
    
bfs(1,V)
    
```

```python
# 방향이 있다면
def bfs(s, V):
    q = [] 					# 큐 생성
    visited = [0] * (V+1) 	# visited 생성
    q.append(s)				# 시작점 인큐
    visited[s] = 1			# 시작점 visited 표시
    while q:				# 큐가 비어있지 않으면 ( 처리할 정점이 남아 있으면)
    	t = q.pop(0)		# 디큐 ( 꺼내서)해서 t에 저장
    	print(t)			# t에 대한 처리
    	for i in range(1, V+1):# t에 인접이고 미방문인 모든 i에
            if adj[t][i] == 1 and visited[i] == 0:
                q.append(i) # enqueue(i)
                visited[i] = visited[t] +1 	# i visited로 표시

V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) in range(V+1)]			# 인접행렬

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adj[n1][n2] = 1
    
bfs(1,V)
```

```python
def bfs(s,V):
    q = [0] * V
    front = -1
    rear = -1
    visited = [0] * (V+1)		# visited 생성
    rear += 1					# ㅅㅣ작점 인큐
    q[rear] = s					
    visited[s] = 1					#시작점 visited
    while front != rear:			# 큐가 비어있지 않으면
        front += 1					# 디큐ㅇ해서 t에 저장
        t = q[front]
        print(t)
        for i in ragne(1, V+1):				# t에 인접하고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:
                rear +=1 					# 인큐 i
                q[rear] = i
                visited[i] = visited[t] +1		# i 방문 표시
        
V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0]*(V+1) in range(V+1)]			# 인접행렬
adjList = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = edge[2*i], edge[2*i+1]
    adj[n1][n2] = 1
    
bfs(1,V)
```

