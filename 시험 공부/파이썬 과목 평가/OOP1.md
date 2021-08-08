# OOP1

객체 지향 (object)

클래스와 객체

1. 객체
   1. 파이썬에서 모든 것은 객체이다.
   2. type / attribute / method를 가진다.
   3. type : 어떤 연산자와 method가 가능한가?
   4. attribute : 어떤 상태를 가지는가?
   5. method : 어떤 행위(함수)를 할 수 있는가?

2. 타입 & 인스턴스 
   1. 타입 : 공통된 attribute와 method를 가진 객체들의 분류
   2. 인스턴스 : 특정 타입의 실제 데이터 예시를 인스턴스라고 한다. // 파이썬에서 모든 객체는 특정 타입의 인스턴스이다.
3. 속성 attribute
   1. 속성은 객체의 상태/데이터를 뜻한다.
   2. complex 복소수 속성 ex ) image_number = 3+4j -> image_number.real = 3 -> image_number.imag = 4
4. 메서드 method
   1. 특정 객체에 적용할 수 있는 행위를 뜻함
   2. <객체>.<메서드>()



### 객체 지향 프로그래밍

- object가 중심이 되는 프로그래밍
- 명령어의 목록으로 보는 시각에서 벗어나 // 여러 개의 독립된 단위, 즉 객체들의 모임으로 파악하고자 함
- 장점 
  - 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용
  - 배우기 쉼고 개발과 보수를 간편하게 만듬
  - 직관적인 코드 분석을 가능하게 함
  - 코드의 **직관성** // 활용의 **용이성** // 변경의 **유연성**



1. 클래스와 인스턴스

   1. 클래스의 생성

      - ```python
        class <클래스 이름>:
            <statement>
        ```

      - ```python
        class Person:
            
        print(type(Person))
        ## <class 'type'>
        ```

   2. 인스턴스의 생성

      1. ```python
         # 인스턴스 = 클래스()
         person1 = Person()
         ```

      2. person1은 인스턴스이다.

      3. ```python
         p1 = Person()
         p2 = Person()
         # ...
         
         print(p1.__doc__)
         print(p2.__doc__)
         ## 이 클래스는 사람을 분류하는 'Person' 클래스입니다.
         ## 이 클래스는 사람을 분류하는 'Person' 클래스입니다.
         ```

      4. ```python
         # Person 클래스와 talk() 메서드를 정의
         class Person:
             def talk(self):
                 print('안녕')
                 
         p1 = Person()
         p2 = Person()
         p3 = Person()
         
         p1.talk()
         p2.talk()
         p3.talk()
         ## 안녕
         ## 안녕
         ## 안녕
         ```

   3. ##### self

      1. 인스턴스 자신(self)

      2. 보통 매개변수 명으로 self 를 첫번째 인자로 정의

         

   4. 생성자 메서드 (```__init__```)

      1. ```python
         class MyClass:
             def __init__(self):
                 print('생성될 때 자동으로 호출되는 메서드입니다.')
         ```

      2. 생성자를 활용하면 인스턴스가 생성될 때 인스턴스의 **속성**을 정의할 수 있습니다.

         

   5. 소멸자 메서드(```__del__```)

      1. ```python
         def __del__(self):
             print('소멸될 때 자동으로 호출되는 메서드입니다.')
         ```

      2. ```python
         # 생성자 메서드는 __init__으로, 소멸자 메서드는 __del__라는 이름으로 정의
         class Person:
             def __init__(self):
                 print('응애!')
                 
             def __del__(self):
                 print('떠날게..')
         ```

      3. ```python
         # 소멸자 호출 -> 매직 메서드 -> 자동으로 호출 ->  내부에 있는 refrence counter가 0이 되는 시점에 호출
         
         del p1
         ## 떠날게..
         ```

   6. 속성 attribute 정의

      1. 특정 데이터 타입 또는 클래스의 객체들이 가지게될 상태/데이터를 의미합니다.

      2. `self.<속성명> = <값>` 혹은 `<인스턴스>.<속성명> = <값>`으로 설정

      3. ```python
         class Person:
             def __init__(self, name):
                 self.name = name
         
             def talk(self):
                 print(f'안녕, 나는 {self.name}')
         ```

      4. ```python
         p1 = Person()
         p2 = Person()
         
         p1.name = 'justin' # <인스턴스>.<속성명> = <값>
         p2.name = 'silver' # <인스턴스>.<속성명> = <값>
         
         p1.talk()
         # print(f'안녕, 나는 {p1.name}')
         p2.talk()
         # print(f'안녕, 나는 {p2.name}')
         ```

      5. 새로운 Person의 인스턴스 p1을 이름과 함께 초기화 하고, 이름을 출력

         ```python
         p1 = Person('silver')
         
         print(p1.name)
         print(p1.talk())
         
         ## silver
         ## 안녕, 나는 silver
         ## None
         ```

      6. 생성자 메서드도 함수이기 때문에, **인자의 개수가 맞지 않으면 에러가 발생**

         ```python
         p1 = Person()
         # self는 넘어갔지만 name 매개변수에 매핑되는 인자를 넘겨주지 않음
         
         #TypeError: __init__() missing 1 required positional argument: 'name'
         ```

   7.  매직(스페셜) 메서드

      1. 더블언더스코어(`__`)가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드이기 때문에 **스페셜 메서드** 혹은 **매직 메서드**라고 불립니다.

      2. 매직(스페셜) 메서드 형태: ```__someting__```

      3. Ex

         ```
         '__str__(self)',
         '__len__(self)',
         '__repr__(self)',
         '__lt__(self, other)',
         '__le__(self, other)',
         '__eq__(self, other)',
         '__ne__(self, other)',
         '__gt__(self, other)',
         '__ge__(self, other)',
         ```

      4. ```__str__(self)```

         1. ```python
            class Person:
                def __str__(self):
                    return '객체 출력(print)시 보여줄 내용'
            ```

         2. ```python
            class Person:
                def __init__(self, name):
                    self.name = name
                
                def __str__(self):
                    # return
                    return f'나는 {self.name}입니다!!!'
                
                def __repr__(self):
                    pass
            ```

         3. ```python
            # 새로운 인스턴스 p2를 생성후 p2를 출력
            p2 = Person('김동현')
            print(p2)
            ## 나는 김동현입니다!!!
            ```

         4. 

