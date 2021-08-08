# OOP2

1. 인스턴스 & 클래스 변수

   1. 인스턴스 변수

      - 인스턴스의 속성

      - 각 인스턴스들의 고유한 변수

      - 생성자 메서드에서 ```self.변수명```으로 정의

      - 인스턴스가 생성된 이후 ```인스턴스.변수명``` 으로 접근 및 할당

      - ```python
        class Person:
        
            def __init__(self, name):    # 인스턴스 메서드 (생성자) 
                self.name = name         # 인스턴스 변수
        ```

      - ``` python
        # Person 클래스의 인스턴스 me, you를 각각 이름과 함께 생성하고, name 속성을 출력
        
        justin = Person('justin') #  self는 자동으로 넘어간다
        silver = Person('silver') # name에 값을 지정한다.
        
        print(justin.name)
        print(silver.name)
        
        ```

   2. 클래스 변수

      - 클래스의 속성

      - 모든 인스턴스가 공유

      - 클래스 선언 내부에서 정의

      - ```클래스.변수명``` 으로 접근 및 할당

      - ```python
        class Circle:
            pi = 3.14
        
        print(Circle.pi)
        ```

      - ```python
        # Circle 클래스의 인스턴스 c1, c2를 생성
        c1 = Circle()
        c2 = Circle()
        
        print(c1.pi) ## 3.14
        print(c2.pi) ## 3.14
        ```

      - ```python
        # c1의 pi 값을 3.141592로 변경
        c1.pi = 3.141592
        
        # c1, c2에서의 pi값을 각각 출력
        print(c1.pi) 		# 3.141592
        print(c2.pi) 		# 3.14
        print(Circle.pi) 	# 3.14
        ```

   3. ##### 인스턴스 & 클래스 간의 이름공간

      1. 클래스를 정의하면 클래스가 생성됨과 동시에 이름공간이 생성
      2. 인스턴스를 만들면 , 객체가 생성되고 해당되는 이름 공간이 생성
      3. 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장
      4. 즉, 인스턴스에서 특정한 어트리뷰트에 접근하게 되면 **인스턴스 -> 클래스** 순으로  탐색

      - ```python
        class Person:
            name = 'unknwon'
            
        # Person 클래스의 인스턴스 p1을 생성하고 name을 확인
        p1 = Person() # Person 클래스의 인스턴스 p1을 생성
        p1.name ## unknown
        
        # p1의 name 속성을 직접 변경하고 확인
        p1.name = 'Jack'
        print(p1.name) #=> 인스턴스의 name
        print(Person.name) #=> 클래스의 name
        ```

2.  ### 메서드의 종류

   1. **인스턴스 메서드**

      1. 인스턴스가 사용할 메서드
      2. 클래스 내부에 정의되는 메서드의 기본값은 인스턴스 메서드
      3. 호출 시, 첫 번째 인자로 **인스턴스 자기 자신 self**가 전달

      

   2. **클래스 메서드**

      1. 클래스가 사용할 메서드

      2. ```python
         @classmethod 을 항상 사용
         ```

      3. 호출 시, 첫 번째 인자로 **클래스 cls**가 전달

      

   3. **스태틱 메서드**

      1. 클래스가 사용할 메서드

      2. ```python
         @staticmethod 을 항상 사용
         ```

      3. 호출 시, 어떠한 인자도 전달되지 않음

      

   4. ```python
      class MyClass:
          def instance_method(self):
              return self
          
          @classmethod
          def class_method(cls):
              return cls
          
          @staticmethod
          def static_method(arg):
              return arg
          
          
      mc = MyClass() # 크래스 -> 인스턴스 생성
      
      print(id(mc.instance_method()), id(mc))
      print(mc.instance_method() == mc) # True
      
      print(id(MyClass.class_method()), id(MyClass))
      print(MyClass.class_method() == MyClass) # True
      
      
      print(MyClass.static_method(1)) # 값 그대로 출력 ## 1
      ```



   			5. 인스턴스와 메서드
         - 인스턴스는 3가지 메서드 모두 접근 가능하다.
         - 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정지어야한다.
         - 되도록 다른 메서드에서 호출되면 안된다.

```python
print(MyClass.instance_method())
# Error => 첫 번째 인자인 인스턴스 객체가 없습니다.


print(MyClass.instance_method(mc))  
# # mc.instance_method()와 같습니다.
```

