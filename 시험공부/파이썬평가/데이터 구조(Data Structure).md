# 데이터 구조(Data Structure)

1. ### 문자열(string)

   1.  조회 탐색 ```.find(x)```

      1.  x의 첫 번째 위치를 반환 / 하지만 **없다면 -1 반환**
      2. ```a.find('p')``` : a 문자열에서 첫 번째 p의 인덱스 값을 반환

   2. .조회 탐색 ```.index()```

      1. x의 첫 번째 위치를 반환 / **없으면 오류 발생**
      2. ```a.index('p')```

   3. 문자열 변경 ```.replace(old, new[, count])```

      1. 바꿀 대상의 글자를 새로운 글자로 바꿔서 반환

      2. ```python
         # 변수명이 a, b인 문자열을 만들어봅시다.
         a = 'yaya!'
         b = 'wooooowoo'
         a.replace('y', 'h') # replace 메서드로 변수 a의 글자 y를 h로 변경
         ```

   4. 문자열 변경 ```.strip([chars])```

      1. 특정한 문자들을 지정하면, 양쪽을 **제거**하거나 왼쪽을 **제거**하거나 오른쪽을 **제거**

      2. ```lstrip``` ```rstrip``` ```strip```

      3. ```python
         a = '   hello!  \n'
         b = 'hihihihahahahihi'
         
         # stript 메서드로 변수 a의 양쪽 공백을 제거
         a.strip()
         
         # lstript 메서드로 변수 a의 왼쪽 공백을 제거
         a.lstrip()
         
         # rstrip 메서드로 변수 b의 오른쪽에서 글자 hi를 제거
         b.rstrip('hi')
         ```

   5. 문자열 변경 ```.split([chars])```

      1. 문자열을 특정한 단위로 나누어 **리스트**로 반환합니다.

      2. ```python
         a = 'a_b_c'
         
         a.split("_")
         # ['a', 'b', 'c']
         
         # 사용자의 입력값을 받아 변수 i에 저장합니다.
         # 입력받은 문자열을 split 메서드로 공백을 기준으로 나누어 리스트로 반환
         nums = input()
         nums = nums.split()
         print(nums) # ['1', '2', '3', '4', '5']
         ```

   6. 문자열 변경 ```'separator'.join(iterable)```

      1. 특정한 문자열로 만들어 반환

      2. 반복 가능한 컨테이너의 요소들을 separator로 합쳐 join 문자열로 반환

      3. ```python
         word = '배고파'
         words = ['안녕', 'hello']
         
         
         # join 메서드로 변수 word의 문자열 사이에 !를 넣은 결과를 반환
         "!".join(word)
         # '배!고!파'
         
         # join 메서드로 변수 words의 문자들을 하나로 합친 결과를 반환
         "".join(words)
         # '안녕hello'
         ```

   7. 문자열 변경  `.capitalize()`, `.title()`, `.upper()`

      1. `.capitalize()` : **앞글자**를 **대문자로** 만들어 반환합니다.
      2. `.title()` : **어포스트로피**나 **공백** 이후를 **대문자로** 만들어 반환합니다.
      3. `.upper()` : **모두 대문자**로 만들어 반환합니다.

   8. 문자열 변경 `.lower()`, `.swapcase()`

      1. `lower()` : **모두 소문자**로 만들어 반환합니다.
      2. `swapcase()` : **대 <-> 소문자로 변경**하여 반환합니다.

   9. ```python
      .isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(), .istitle(), .islower()
      
      ```





### 2. 리스트

1. ```.append(x)``` : 값 추가 및 삭제

   1. ```python
      cafe = ['starbucks', 'tomntoms', 'hollys']
      cafe.append('banapresso')
      print(cafe)
      # ['starbucks', 'tomntoms', 'hollys', 'banapresso', 'banapresso']
      ```

2. ```.extend(iterable)``` 

   1. 리스트에 iterable(list, range, tupel, string)  값을 붙일 수 있습니다.
   2. append & extend 차이점
      1. 리스트로 입력을 했을 때
         - append : 리스트 통째로 들어간다.
         - extend : 리스트 안에 요소만 들어간다.
      2. 문자열로 추가했을 때
         - append : 문자열로 들어간다.
         - extend : 문자열의 문자 하나 하나 리스트의 요소로 들어간다.

3. ```.insert(i, x)```

   1. 정해진 위치 i에 x값을 추가합니다.

   2. ```python
      # insert 메서드로 변수 cafe 첫번째에 문자열 start
      cafe.insert(0, 'start')
      print(cafe)
      
      # cafe[0]에 start 문자열 추가
      ```

   3. ```python
      # insert 메서드로 변수 cafe 마지막에 문자열 end
      # 마지막 위치는 len함수를 이용
      cafe.insert(len(cafe), 'end')
      print(cafe)
      
      # 맨 마지막 부분에 end 문자열 추가
      ```

4.  ```.remove(x)```

   1. 리스트에서 값이 x인 것을 삭제

   2. ```python
      numbers = [1, 2, 3, 1, 2]
      
      numbers.remove(1)
      print(numbers) # [2, 3, 1, 2]
      
      numbers.remove(1)
      print(numbers) # [2, 3, 2]
      
      # remove 메서드로 1을 한번 더 삭제
      # remove는 값이 없으면 오류가 발생
      numbers.remove(1)
      print(numbers)
      ```

5. ```.pop(i)```

   1. 정해진 위치 i에 있는 값을 삭제하며, 그 항목을 반환

   2. i가 지정되지 않으면 마지막 항목을 삭제하고 되돌려준다.

   3. ```python
      numbers = [1, 2, 3, 4, 5, 6]
      
      # pop 메서드로 가장 앞에 있는 숫자을 삭제
      # 삭제 후 변수 numbers를 출력
      result = numbers.pop(0)
      print(result) 		# 1
      print(numbers) 		# [2, 3, 4, 5, 6]
      
      # pop 메서드로 가장 마지막에 있는 숫자를 삭제하고 결과를 변수 a 에 저장
      # 삭제된 숫자와 결과를 모두 출력
      result = numbers.pop() 	# 6
      print(result) 			# [2, 3, 4, 5]
      ```

6. ```.clear()``` : 리스트의 모든 항목을 삭제

7. ```.count(x)``` : 원하는 값의 개수를 반환

8. ```.sort()``` : 정렬 / ```sorted()```와 다르게 **원본 리스트를 변형**하고 None값을 리턴 

   ```nums.sort(reverse=False)``` : 오름차순

   ```nums.sort(reverse=Ture)``` : 내림차순

9. ```.reverse()``` : 반대로 뒤집는다. 정렬은 아님



### 3. 데이터의 분류

1. immutable 변경 불가능한 데이터

   1. literal : 숫자 / 글자 / 참거짓
   2. range()
   3. tuple()
   4. frozenset()

2. mutable 변경 가능한 데이터

   1. list
   2. dict
   3. set

3. 리스트 복사 방법 **(복사한 원본에 영향을 끼치지 않으며)**

   1. **slice 연산자** 사용

      -  ```python
         a = [1, 2, 3]
         
         # slice 연산자로 리스트 a의 모든 요소를 변수 b에 저장합니다.
         # 리스트 b의 첫번째 값을 5로 바꾸고 리스트 a를 출력합니다.
         # slice 연산자를 활용하면 새로운 리스트를 저장할 수 있습니다.
         # ===== 
         b = a[:] # 중요
         
         b[0] = 5
         print(a)
         print(b)
         
         # a는 변하지 않고 복사해서 b만 변경할 수 있음 
         # [1, 2, 3]
         # [5, 2, 3]
         ```

   2. **list() **활용

      - ```python
        a = [1, 2, 3]
        
        # list 함수로 리스트 a를 복사하여 변수 b에 저장합니다.
        # 리스트 b의 첫번째 값을 5로 바꾸고 리스트 a를 출력합니다.
        # ===== 
        b = list(a) # 포인트
        
        b[0] = 5
        print(a)
        print(b)
        
        # a는 변하지 않고 복사해서 b만 변경할 수 있음 
        # [1, 2, 3]
        # [5, 2, 3]
        ```

   3. **copy() **활용

      1. ```python
         import copy
         
         a= [1,2,3]
         
         b= copy.copy(a)
         b[0] = 5
         
         print(a)
         print(b)
         
         # [1, 2, 3]
         # [5, 2, 3]
         ```

   4. 하지만, 이렇게 하는 것도 일부 상황에만 서로 `다른 얕은 복사(shallow copy)`입니다.

   5. 깊은 복사도 할 수 있음

      - ```python
        ### copy.deepcopy
        
        import copy
        
        a = [1, 2, [1, 2]]
        b = copy.deepcopy(a)
        
        b[2][0] = 3
        print(a)
        print(b)
        
        # [1, 2, [1, 2]]
        # [1, 2, [3, 2]]
        ```



### 4. List Comprehension

1. ```python
   [expression for 변수 in iterable]
   
   list(expression for 변수 in iterable)
   ```

2. ```python
   # 세제곱 리스트
   cubic_list= [num**3 for num in numbers]
   print(cubic_list)
   
   # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
   ```

3. 조건식

   - ```python
     [expression for 변수 in iterable if 조건식]
     ```

   - ```python
     even_list = [num for num in numbers if num%2==0]
     ```



### 5. 데이터 구조에 적용 가능한 Built in Function

1. 순회 가능한 iterable 데이터ㅓ 구조에 적용 가능한 ~

2. iterable 타입 - `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range`

3. ```map(function, iterable)``` 

   1. 순회 가증한 데이터 구조의 모든 요소에 function을 적용한 후 그 결과를 반환

   2. return은 map_object 형태이다.

   3. ```python
      numbers = [1, 2, 3]
      
      my_num_str = "".join([str(num) for num in numbers ]) 
      
      my_num_str = list(map(str, numbers))
      
      print(my_num_str)
      ```

   4. ```python
      # 세제곱의 결과를 나타내는 함수가 있습니다.
      def cube(n):
          return n ** 3
      
      # 세제곱 함수를 각각의 요소에 적용한 결과값을 구해봅시다.
      numbers = [1, 2, 3]
      
      new_numbers = list(map(cube, numbers))
      print(new_numbers) # [1, 8, 27]
      ```

   5. 두 정수를 입력 받는다.

      ```python
      nums = list(map(int, input().split()))
      ```

4. ```filter(function, iterable)```

   1. iterable에서 function의 반환된 결과가 **True** 인 것들만 반환

   2. ```python
      # 홀수를 판별하는 함수가 있습니다.
      def odd(n):
          return n % 2
      
      # 홀수인 요소만 뽑아 new_numbers에 저장합니다.
      numbers = [1, 2, 3]
      
      new_numbers = list(filter(odd, numbers))
      print(new_numbers) 			# [1, 3]
      ```

   3. map 함수와의 차이점

      1. ```python
         new_numbers_map = list(map(odd, numbers))
         print(new_numbers_map)
         
         # odd 함수 결과에 맞게 나머지를 반환함.
         ```

5. ```zip(*iterable)```

   1. 복수의 iterable 객체를 모아 zip 합니다.

   2. 결과는 튜플의 모음으로 구성된 zip object 반환

   3. ```python
      girls = ['jane', 'ashley', 'mary']
      boys = ['justin', 'eric', 'david']
      
      pair = list(zip(girls, boys))
      print(pair)
      
      # [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
      ```

   4. 만약 숫자가 맞지 않는 경우에는  넘치는 부분 zip하지 않는다.

