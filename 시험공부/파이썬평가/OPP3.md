# OPP3

- 상속
- 메서드 오버라이딩
- 다중 상속



1. 상속

   1. 클래스에서 가장 큰 특징은 상속이 가능하다는 것이다.

   2. 부모 클래스의 속성이 자식 클래스에 상속되어 코드 재사용성이 높아짐

   3. ```python
      class ChildClass(ParentClass):
          <code block>
      ```

   4. ```python
      class Person:
          population = 0
          
          def __init__(self, name='사람'):
              self.name = name
              Person.population += 1
              
          def talk(self):
              print(f'반갑습니다. {self.name}입니다.')
       
      
      
      # Person 클래스의 인스턴스 p1을 생성해봅시다.
      # name 속성은 자유롭게 설정합니다.        
      runkey = Person('runkey')
      runkey.talk()
      ```

   5. ```python
      class Student(Person):
          def __init__(self, student_id, name='학생'):
              self.name = name
              self.student_id = student_id  
              Person.population += 1
              
              
      print(runkey.name, runkey.student_id)
      # 자식 클래스의 인스턴스는 부모 클래스에 정의된 메서드를 호출 할 수 있다.
      
      runkey.talk() # 상속의 핵심
      ```

   6. issumblass(class, classinfo)

      - class 가 classinfo의 subclass이라면 True

   7. isinstance(object, classinfo)

      - object가 classinfo의 인스턴스이거나 subclass인 경우 True

   8. issubclass 함수를 통해 Student 클래스와 Person 클래스가 상속관계인지 확인 가능

   ```python
   issubclass(Student, Person)
   ## True
   
   # class 자리에 자식 클래스가 오면 False로 나타난다.
   ```

   9. super()

      1. 자식 클래스에 메서드를 추가로 구현할 수 있다.

      2. 부모 클래스의 내용을 사용하고자 할 대. super()를 사용할 수 있다.

      3. ```python
         class ChildClass(ParentClass):
             def method(self, arg):
                 super().method(arg) # 부모클래스의 메서드를 가져와서 사용할 수 있다
         ```

      4. ```python
         class Person:
             def __init__(self, name, age, number, email):
                 self.name = name
                 self.age = age
                 self.number = number
                 self.email = email 
                 
             def greeting(self):
                 print(f'안녕, {self.name}')
                 
                 
         class Student(Person):
             def __init__(self, name, age, number, email, student_id):
                 # Person 클래스 부모 클래스를 호출했다.
                 super().__init__(name, age, number, email) # 동일한 코드를 줄일 수 있다.
                 self.student_id = student_id
                 
                 
         ```

2. 메서드 오버라이딩

   - 자식 클래스에서 부모클래스의 메서드를 재정의하는 것
     - 상속 받은 메서드를 재정의할 수도 있습니다.
     - 상속 받은 클래스에서 같은 이름의 메서드로 덮어씁니다.

