# 데이터 구조(Data Structure) 2

1. 세트(set)

   1. .add(elem) : elem을 세트에 추가한다.

   2. .update(*others) : 여러 값을 세트에 추가한다. / 반드시 iterable 데이터 구조를 전달해야함

   3. .remove(elem) : elem을 삭제하고 없으면 **keyerror**가 발생

   4. .discard(elem) : elem을 세트에서 삭제하고 // 없어도 에러 발생하지 않음

   5. .pop() : **임의의 원소**를 제거해서 반환한다.

      

2. 딕셔너리

   1. .get(key[,default]) : key를 통해 value를 가져옵니다. /절대로 에러 발생하지 않음 / default = none

      - 업으면 없다고 뜬다 / 에러 발생하지 않음
      - default 값에 다른 수를 넣어주면 없을 때 해당 값이 뜸

   2. .pop(key[,default]) : key가 딕셔너리에 있으면 제거하고 그 값을 반환합니다. 그렇지 않으면 default 값을 반환합니다. 

      - default 값이 없는 상태에서 딕셔너리에 없으면 key error 발생합니다.

   3. .update() : 값을 제공하는 key, value를 덮어씁니다.

      - ```python
        my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
        
        my_dict.update({'apple' : '사과아'})
        my_dict.update(grape = '포도오')
        
        print(my_dict)
        # {'apple': '사과아', 'banana': '바나나', 'melon': '멜론', 'grape': '포도오'}
        ```

   4. ##### 딕셔너리 순회

      1. ```python
         grades = {'john':  80, 'eric': 90, 'justin': 100}
         
         for student in grades:
             print(student)
         # john
         # eric
         # justin ## key 값이 출력된다.
         
         for student in grades:
             print(grades[student])
         #80
         #90
         #100   ## value 값이 출력된다.  
         ```

      2. 









# 정리

문자열 / 리스트 / 빌트인 함수  / 셋 / 딕셔너리 / 

1. 문자열 : **immutable // ordered // iterable**
   1. .find(x) : x의 첫 번째 위치 인덱스를 반환
   2. .index(x) : x의 첫 번째 위치 인덱스를 반환 / 하지만 없으면 오류 발생
   3. .replace(old, new[, count]) : old를 new로 변환 / 따로 개수를 정할 수 있음
   4. .strip([char]) : 해당 문자열을 양쪽에서 제거
   5. .lstrip : 왼쪽에서 제거
   6. .rstrip : 오른쪽에서 제거
   7. .split([char]) : 문자열을 쪼개서 리스트로 반환
   8. .join(iterable) : 리스트로 쪼개진 요소들을 한 문자열로 반환
   9. .capitalize() : 맨 앞 첫 글자만 대문자 변환
   10. .title() : 공백 , ' ' 등의 표기 이후 대문자 변환
   11. .upper() : 전부 대문자 변환
   12. .lower() : 전부 소문자 변환
   13. .swapcase() : 대문자는 소문자로 소문자는 대문자로
2. 리스트 : **mutable // ordered // iterable**
   1. .append(x) : x를 리스트에 추가
   2. .extend(iterable) : iterable을 리스트에 추가
   3. .insert(i, x)
   4. .remove(x)
   5. .pop(i)
   6. .clear()
   7. .index()
   8. .count(x)
   9. .sort()
   10. .reverse()
3. 셋 set : **mutable // unordered // iterable**
   1. .add(elem)
   2. .update(*other)
   3. .remove(elem)
   4. .discard(elem)
   5. .pop()
4. 딕셔너리 : **mutable // unordered // iterable**
   1. .get(key[, default])
   2. .pop(key[, default])
   3. .update()
   4. 
