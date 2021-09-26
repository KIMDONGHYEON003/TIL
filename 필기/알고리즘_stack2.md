# stack2

- 계산기
- 백트래킹
- [참고]부분집합, 순열
- 분할정복



##### 계산기

- 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있다.
- 문자열 수식 계산의 일반적 방법
  - step1. 중위 표기법의 수식을 후위 표기법으로 변경한다(스택 이용)
  - step2. 후위 표기법의 수식을 스택을 이용하여 계산한다.
- 중위 표기법(infix notation)
  - 연산자를 피연산자의 가운데 표기하는 방법 (a+b)
- 후위 표기법(postfix notation)
  - 연산자를 피연산자 뒤에 표기(ab+)



- 중위 표기식에서 후위표기식으로 변경 방법
  1. 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현
  2. 각 연산자를 그에 대응하는 



- 중위 표기식에서 후위표기식으로 변경 방법(스택이용)
  1. ㅂ입력받은 주우이 표기식에서 토큰을 읽는다.
  2. 토큰이 피연산자이면 토큰을 출력
  3. 토큰이 연산자(괄호포함)일 때, 이토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
  4. 토큰이 오른쪽 괄호 ) 이면 스택 top에 왼쪽 괄호 (가~~
  5. 그림으로









백 트래팅

- 미로찾기

- 백트래팅과 깊이 우선 탐색과의 차이

  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임(가지치기)
  - 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
  - 깊이 우선 탐색을 가하기에는 경우의 수가 너무나 많음 즉, N! 가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능한 문제
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이역시 최악의 경우에는 여전히 지수 함수 시간을 요하므로 처리 불가능

- 백 트래킹을 이용한 알고리즘 절차

  - 상태 공간 트리의 깊이 우선 검색을 실시
  - 각 노드가 유망한지
  - 유망하지 않으면 부모 노드로 가서 한다.

- ```python
  def checknode(v): 
      if promising(v):
          if there is a solution at v:
          	write the solution
          else:
              for u in each child of v:
                  checknode(u)
  ```



부분집합 구하기

- 백트래킹 기법으로 powerset을 구해보자
  - 앞에서 설명한 일반적인 백트래팅 접근 방법을 이용
  - n개의 원소가 들어있는 집합의 2**n개의 부분집합을 만들 때는 , treu 또는 false값을 가지는 항복들로 구성된 n개의 배열을 만드는 방법을 이용
  - 여기서 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값이다.

- ```python
  def backtrack(a, k, input):
      global MAXCANDIDATES
      c = [0] * MAXCANDIDATES
      
      if k == input:
          process_solution(a,k) #답이면 원하는 작업을 한다.
      else:
          k+=1
          ncandidates = construct_candidates(a,k,input,c)
          for i in range
  ```

- 



거듣제곱

```python
def Power(Base, Exponent):
    if Base == 0:
        return 1
    result = 1	
    for i in range(Exponent):
        result *= Base
    return result
```

```python
def Power(Base, Exponent):
    if Exponent == 0 or Base --0:
        return1
    if Exponent %2 ==0:
        NewBase = Power(Base, Expoenet/2)
        return NewBase **2
    
```

