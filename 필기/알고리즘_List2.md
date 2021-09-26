# 알고리즘

## List2

 

1. 2차원 배열 서언

   - 1차원 List를 묶어 놓음

   - 2차원 이상의 다차원 List는 차원에 따라 Index 선언

   - 2차원 List의 선언 : 세로길이(행의 개수), 가로 길이(열의 개수)를 필요로 함

   - Python에서는 데이터 초기화를 통해 변수 선언과 초기화가 가능함

   - ```arr = [[0,1,2,3],[4,5,6,7]]```

   - ```python
     N, M = map(int, input().split())
     arr = [list(map(int, input().split())) for _ in range(N)]
     print(arr)
     ```

   - 

2. 배열 순회

   - n X m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

3. 행 우선 순회

   - ```python
     for i in range(len(array)):
         for j int range(len(array[i])):
             array[i][j]
             
     ```

4. 열 우선 순회

   - ```python
     for j in range(len(array[0])):
         for i in range(len(array)):
             array[i][j]
     ```

5. 지그재그 순회

   - ```python
     for i in range(len(array)):
     	for j in range(len(array)):
             array[i][j + (m-1-2*j) * (i%2)]
     ```

6. 델타를 이용한 2차 배열 탐색

   - 2차 배열이 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

   - ```python
     ary[0...n-1][0...n-1]
     
     dx[] = [0,0,-1,1]
     dy[] = [-1,1,0,0] #좌우 상하
     
     for x in range(len(ary)):
         for y in range(len(ary[x])):
             for I in range(4): # 총 네 방향에 접근할 것이다.
                 textX = x+dx[mode]
                 textY = y+dy[mode]
                 print(ary[textX][testY])
                 if 0 <= testX < len(ary) and 0 <= testY <= len(ary[x]):
                     ary[testX][testY]
                     
     for x in range(len(ary)):
         for j in range(len(ary[x])):
             for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                 testX = x + dr
                 testY = y + dc
                 if 0 <= testX < len(ary) and 0< = testY < len(ary[x]):
                     ary[testX][testY]
     ```

7. 전치행렬

   - ```python
     arr = [[1,2,3],[4,5,6],[7,8,9]]
     
     for i in range(3):
         for j in range(3):
             if i < j:
                 arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
     ```

8. 부분집합의 수

   1. 집합의 원소가 n개 일 때, 공집합을 포함한 부분집합의 수는 2**n 개이다.

   2. 이는 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수와 같다.

   3. ex ) {1,2,3,4} => 2 * 2 * 2 * 2 = 16 가지

   4. 부분집합 생성하기

      - 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 방법

      - ```python
        bit = [0,0,0,0]
        for i in range(2):
            bit[0] = i					# 0 번째 원소
            for j in range(2):
                bit[1] = j				# 1 번째 원소
                for k in range(2):
                    bit[2] = k			# 2 번째 원소
                    for l in range(2):
                        bit[3] = 1		# 3 번째 원소
                        print(bit, end= ' ')		# 생성된 부분집합 출력
                        
                        for p in range(4):
                            if bit[p]:	# 1이면!!
                                print(arr[p], end=' ')
                        print()
                        
        # 0000 부터 1111까지 모두 출력할 수 있음
        ```
        
        ```python
        for i in range(1, 1<< N):
            for j in range(N):
                if i & (1 << j):
                    print(ingredients[j], end='')
            print()
        ```
        
        

9. 비트 연산자

   - & : 비트 단위로 and 연산

   - | : 비트 단위로 or 연산

   - << : 피연산자의 비트 열을 왼쪽으로 이동

   - '>>' : 피 연산자의 비트 열을 오른쪽으로 이동

   - 1<<n : 2^n 원소가 n개일 경우 모든 부분집합의 수를 의미 ex> 1<<3 : 2^3

   - i & (1<<j) : i의 j번째 비트가 1인지 아닌지를 리턴한다.

   - ```python
     arr = [3,6,7,1,5,4]
     
     n = len(arr)					#n의 원소의 개수
     
     for i in range(1<<n):			#1<<n : 부분 집합의 개수
         for j in range(n):		# 원소의 수만큼 비트를 비교함
             if i & (1<<j):			# i의 j번째 비트가 1이면 j번재 원소 출력
                 print(arr[j], end=", ")
             print()
        	print()
     ```

10. 검색

    - 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

    - 목적하는 탐색 키를 가진 항목을 찾는 것

      - 탐색 키 : 자료를 구별하여 인식할 수 있는 키

    - 검색의 종류

      - 순차 검색
      - 이진 검색
      - 해쉬

    - 순차 검색 

      - 일렬로 되어 있는 자료를 순서대로 검색

        - 가장 간단하고 직관적임
        - 배열이나 연결 리스트 등 순차 구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
        - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임

      - 2가지 경우

        - 정렬되어 있지 않은 경우

          - 찾고자 하는 원소의 순서에 따라 비교 회수가 결정

            - 첫 번째 원소를 찾을 때는 1번 ~~

            - 정렬되지 않은 사료에서의 순차 검색의 평균 비교 회수

              -  = (1/n) * (1+2+3+...+n) = (n+1)/2

            - 시간 복잡도  O(n)

            - ```python
              def squentialSearch(a,n,key):
                  i = 0
                  while i<n and a[i] != key:
                      i = i+1
                  if i <n : return i	# 찾은 경우
                  else: return -1		# 실패한 경우
              ```

        - 정렬되어 있는 경우

          - 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정하자

          - 자료를 순차적으로 검색하면 키 값을 비교하여, 원소의 키 값이 ~ 종료 조건이 하나 는다. 종료 조건 key 보다 큰 값인 경우

          - ```python
            def sequentialSearch2(a, n, key):
                i = 0
                while i<n and a[i]<key:
                    i = i+1
                	if i<n and a[i] = key:		# 
                        return i
                    elif a[i] >key
                        return -1
                return -1
            ```

11. 2진 검색

    - 자료의 **가운데**에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

      - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

    - 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

    - 계속해서 절반을 짤라서 검색한다고 생각하면 편함

    - 검색과정

      - 자료 중앙에 있는 원소를 고른다
      - 중앙 원소의 값과 찾고자 하는 목표 값을 비교 
      - 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행 / 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행
      - 찾고자 하는 값을 찾을 때까지 1-3 과정을 반복

    - ```python
      def binarySearch(a, key):
          start = 0
          end = length(a)-1
          while start <= end:
              middle = (start +end ) // 2
              if a[middle] == key:		# 검색 성공
                  return true
              elif a[middle] > key:
                  end = middle -1
              else:
                  start = middel + 1
          return False					# 검색 실패
      ```

    - 

12. 인덱스

    - 인덱스라는 용어는 데이터베이스에서 유래, 테이블에 대한 동작 속도를 높여주는 자료구조
    - 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다. 왜냐하면 보통 인덱스는 키 필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문
    - 배열을 사용한 인덱스

13. **선택정렬**

    1. 정리하는 느낌

    2. 많은 사람들은 당구대 위에 있는 공 중 가장 작은 숫자의 공부터 골라서 정리할 것이다. 이것이 바로 선택정렬~

    3. 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

       - 셀렉션 알고리즘을 전체 자료에 적용한 것

    4. 정렬과정

       1. 주어진 리스트 중에서 최소값을 찾는다.
       2. 그 값을 리스트의 맨 앞에 위치한 값과 **교환** (밀리는 것이 아닌 바뀌는 것)
       3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복

    5. 시간 복잡도 : O(n2)

    6. ```python
       def SelectionSort(a)
           for i range(0,len(a)-1):					# 작업 구간의 시작
               min = i									# 맨 앞을 제일 작다고 가정
               for j in range(i+1, len(a)):
                   if a[min] > a[j]:
                       min = j
               a[i], a[min] = a[min], a[i]
       ```

14. 셀렉션 알고리즘

    - 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법

    - 최소값 최대값 혹은 중간값을 

    - 선택과정

      - 정렬 알고리즘으로 자료 정렬
      - 원하는 순서에 있는 원소 가져오기

    - 1번 부터 k번재까지 작은 원소들을 찾아 배열의 앞쪽으로 이동, 배열의 k번째를 반환

    - k가 비교적 작을 때 유용하며 O(kn) 수행시간 필요

    - ```python
      def select(list, k):
          for i in range(0,k):
              minIndex = i
              for j in range(i+1, len(list)):
                  if list[minIndex] > list[j]:
                      minIndex = j
              list[i], list[minIndex] = list[minIndex], list[i]
          return list[k-1]
      ```

15. 달팽이 정렬

    1. di dj를 이용한 방법

    2. 방향을 4가지 받는데 처음엔 0번 방향으로 움직이다가 갈 곳이 없으면 1번 방향으로

    3. 갈 곳이 없다는 것은 영역을 벗어나는 경우 / 이미 숫자가 있는 경우

    4. 다른방법

    5. 0,0에서 시작하지 말고 0,-1에서 시작하면 처음에 0의 방향으로 이동핼 할 때 0,0에 들어가서 이동f

    6. 다른방법

    7. 5-4-3-2-1 길이가 줄어든다 / 열 증가 -> 행증가 -> 열감소 -> 행감소 -> 열증가

    8. ```python
       di = [0,1,0,-1]
       dj = [1,0,-1,0]
       
       N = 5
       cnt = 1
       i, j = 0, -1
       k = 0
       while cnt <= N*M:
           ni, nj = i + di[k], j + dj[k]
           if ni, nj가 유효하고 and A[ni][nj] == 0:
               A[ni][nj] = cnt
               cnt += 1
               i, j = ni, nj
           else:
               k = (k+1) % 4
       ```

    9. 

