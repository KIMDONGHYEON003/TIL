[TOC]

# SQL with django ORM

## 기본 준비 사항

```bash
# 폴더구조

99_sql # only SQL
    hellodb.csv
    tutorial.sqlite3
    users.csv
99_sql_orm # SQL + ORM
    ...
    users.csv # 해당 디렉토리로 다운로드
```

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
    $ python manage.py sqlmigrate users 0001
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```

* 확인

  * sqlite3에서 스키마 확인

    ```sqlite
    sqlite > .schema users_user
    CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
    ```



---



## 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **vscode 터미널을 좌/우로 나누어 진행하시오. (sqlite / shell_plus)**

`.headers on` 만 켜고 작성해주세요.



### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   https://docs.djangoproject.com/en/3.2/ref/models/querysets/#all

   ```python
   # orm
   
   In [7]: User.objects.all()
   Out[7]: <QuerySet [<User: User object (1)>, <User: 
   User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>, <User: User object (6)>, <User: User object (7)>, <User: User object (8)>, <User: User object (9)>, <User: User object (10)>, <User: User object (11)>, <User: User object (12)>, <User: User object (13)>, <User: User object (14)>, <User: User object (15)>, <User: User object (16)>, <User: User object (17)>, <User: 
   User object (18)>, <User: User object (19)>, <User: User object (20)>, '...(remaining elements truncated)...']>
   ```

      ```sql
   -- sql
   
   SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   
   In [8]: User.objects.create(first_name='길동',
      ...: last_name='홍',
      ...: age=100,
      ...: country='제주도',
      ...: phone='010-1234-1234',
      ...: balance=10000,
      ...: )
   Out[8]: <User: User object (101)>
   ```

   ```sql
   -- sql
   
   sqlite> INSERT INTO users_user VALUES (102, '길동', '김', 100, '경상북도', '010-1234-1234', 100);
   
   -- 1. id를 명시했기 때문에 넣어주어야 한다.
   sqlite> INSERT INTO users_user
      ...> VALUES ('길동', '홍', 100, '제주도', '010-1234-123  4
   ', 100000);
   Error: table users_user has 7 columns but 6 values were supplied
   
   -- 2. 기존 id에 데이터를 insert 하려고 해도 오류가 발생한다. (고유값을 중복해서 생성할 수 없음)
   sqlite> INSERT INTO users_user
      ...> VALUES (101, '길동', '홍', 100, '제주도', '010-1234
   -1234', 10000);
   Error: UNIQUE constraint failed: users_user.id
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `101` 번 id의 전체 레코드 조회

   ```python
   # orm
   
   In [9]: User.objects.get(pk=101)
   Out[9]: <User: User object (101)>
           
   In [10]: User.objects.get(pk=101).first_name
   Out[10]: '길동'
   
   In [11]: User.objects.get(pk=101).country
   Out[11]: '제주도'
   ```

   ```sql
   -- sql
   
   sqlite> SELECT * FROM users_user WHERE id=101;
   ```

4. 해당 user 레코드 수정

   - ORM: `101` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `101` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   
   In [12]: user = User.objects.get(pk=101)
   
   In [13]: user
   Out[13]: <User: User object (101)>
   
   In [14]: user.last_name = '김'
   
   In [15]: user.last_name
   Out[15]: '김'
   
   # save 메서드를 호출해야 실제 DB에 저장
   In [16]: user.save()
   
   In [17]: user.last_name
   ```

      ```sql
   -- sql
   
   sqlite> UPDATE users_user
      ...> SET first_name='철수'
      ...> WHERE id=101
   
   sqlite> SELECT first_name FROM users_user WHERE id=101;    
   first_name
   "철수"
      ```

5. 해당 user 레코드 삭제

   https://docs.djangoproject.com/en/3.2/ref/models/querysets/#delete

   - ORM: `101` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 (ORM에서 삭제가 되었기 때문에 아무런 응답이 없음)

   ```python
   # orm
   
   In [18]: User.objects.get(pk=101).delete()
   Out[18]: (1, {'users.User': 1})
   
   # get은 반드시 고유한 값에 사용해야 한다.
   # 없어도
   In [19]: User.objects.get(pk=101)
   DoesNotExist: User matching query does not exist.
   
   # 2개 이상이어도 안된다!
   In [20]: User.objects.get(last_name='김')
   MultipleObjectsReturned: get() returned more than one User -- it returned more than 20!
   ```

   ```sql
   -- sql
   
   sqlite> DELETE FROM users_user
      ...> WHERE id=101;
   sqlite> SELECT * FROM users_user WHERE id=101;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   https://docs.djangoproject.com/en/3.1/ref/models/querysets/#count

   - `User` 의 전체 인원수

   ```python
   # orm
   
   In [22]: User.objects.count()
   Out[22]: 101
       
   In [23]: len(User.objects.all())
   Out[23]: 101
       
   # count() vs len()
   A count() call performs a SELECT COUNT(*) behind the scenes, so you should always use count() rather than loading all of the record into Python objects and calling len() on the result (unless you need to load the objects into memory anyway, in which case len() will be faster).
   
   Note that if you want the number of items in a QuerySet and are also retrieving model instances from it (for example, by iterating over it), it’s probably more efficient to use len(queryset) which won’t cause an extra database query like count() would.
   ```

   ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user;
   COUNT(*)
   101
   ```

2. 나이가 30인 사람의 이름

   https://docs.djangoproject.com/en/3.2/ref/models/querysets/#values

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   
   In [25]: User.objects.filter(age=30).values()
   Out[25]: <QuerySet [{'id': 5, 'first_name': '영환', 'last_name': '차', 'age': 30, 'country': '충청북도', 'phone': '011-2921-4284', 'balance': 220}, {'id': 57, 'first_name': '보람', 'last_name': '안', 'age': 30, 'country': '제주특별자치도', 'phone': '010-6132-4229', 'balance': 68000}, {'id': 60, 'first_name': '은영', 'last_name': '김', 'age': 30, 'country': '경상북도', 'phone': '02-5110-2334', 'balance': 350}]>
       
   In [26]: User.objects.filter(age=30).values('first_name')
   Out[26]: <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': ' 
   은영'}]>
   
   In [27]: User.objects.filter(age=30).values('first_name', 'last_name')
   Out[27]: <QuerySet [{'first_name': '영환', 'last_name': '차'}, {'first_name': '보람', 'last_name': '안'}, {'first_name': '은영', 'last_name': '김'}]>
                                                                    
   In [28]: print(User.objects.filter(age=30).values('first_name', 'last_name').query)  
   SELECT "users_user"."first_name", "users_user"."last_name" FROM "users_user" WHERE "users_user"."age" = 30
                                                                    
                                                                    
   In [29]: user = User.objects.filter(age=30).values('first_name')
   
   In [30]: user
   Out[30]: <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': ' 
   은영'}]>
   
   In [31]: user.first()
   Out[31]: {'first_name': '영환'}
   
   In [32]: user.first().get('first_name')
   Out[32]: '영환'
   
   ```

   ```sql
   -- sql
   
   sqlite> SELECT first_name FROM users_user WHERE age=30;    
   first_name
   "영환"
   "보람"
   "은영"
   ```

3. 나이가 30살 이상인 사람의 인원 수

   https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   
   In [34]: User.objects.filter(age__gte=30).count()
   Out[34]: 44
   
   In [36]: print(User.objects.filter(age__gte=30).query)
   SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user" WHERE "users_user"."age" >= 30
   ```

   ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user WHERE age >= 30;   
   COUNT(*)
   44
   ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   
   In [37]: User.objects.filter(age__lte=20).count()
   Out[37]: 23
   ```

   ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user WHERE age <= 20;   
   COUNT(*)
   23
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   
   # 방법 1
   In [38]: User.objects.filter(age=30, last_name='김').count()
   Out[38]: 1
       
   In [39]: print(User.objects.filter(age=30, last_name='김').query)
   SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user" WHERE ("users_user"."age" = 30 AND "users_user"."last_name" = 김)
   
   # 방법 2
   In [40]: User.objects.filter(age=30)
   Out[40]: <QuerySet [<User: User object (5)>, <User: User object (57)>, <User: User object (60)>]>
   
   In [41]: User.objects.filter(age=30).filter(last_name='김')
   Out[41]: <QuerySet [<User: User object (60)>]>
   
   In [42]: User.objects.filter(age=30).filter(last_name='김').count()
   Out[42]: 1
   ```

      ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user
      ...> WHERE age = 30 AND last_name = '김';
   COUNT(*)
   1
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   https://docs.djangoproject.com/en/3.2/topics/db/queries/#complex-lookups-with-q-objects

   https://docs.djangoproject.com/en/3.2/ref/models/querysets/#operators-that-return-new-querysets

   ```
   A Q object (django.db.models.Q) is an object used to encapsulate a collection of keyword arguments. They make it possible to define and reuse conditions, and combine them using operators such as | (OR) and & (AND). Complex lookups with Q objects
   ```

   ```python
   # orm
   # 만약 OR를 사용하고 싶다면? => Q Object 사용해야 합니다!
   # 나이가 30살이거나 성이 김씨인 사람은?
   In [43]: from django.db.models import Q
   
   In [44]: User.objects.filter(Q(age=30) | Q(last_name='김'))
   Out[44]: <QuerySet [<User: User object (5)>, <User: User object (8)>, <User: User object (9)>, <User: User object (11)>, <User: User object (14)>, <User: User object (16)>, <User: User object (18)>, <User: User object (19)>, <User: User object (20)>, <User: User object (23)>, <User: User object (32)>, <User: User object (46)>, <User: User object (47)>, <User: User object (57)>, <User: User object (60)>, <User: User object (62)>, <User: User object (70)>, <User: User object (78)>, <User: User object (82)>, <User: User object (85)>, '...(remaining elements truncated)...']>
   
   In [45]: User.objects.filter(Q(age=30) | Q(last_name='김')).count()
   Out[45]: 26
       
   In [46]: print(User.objects.filter(Q(age=30) | Q(last_name='김')).query)
   SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user" WHERE ("users_user"."age" = 30 OR "users_user"."last_name" = 김)  
   ```
   
   ```sql
   -- sql
   
   sqlite> SELECT * FROM users_user
      ...> WHERE age = 30 OR last_name = '김';
   id,first_name,last_name,age,country,phone,balance
   5,"영환","차",30,"충청북도",011-2921-4284,220
   8,"예진","김",33,"충청북도",010-5123-9107,3700
   9,"서현","김",23,"제주특별자치도",016-6839-1106,43000      
   11,"서영","김",15,"제주특별자치도",016-3046-9822,640000    
   ...
   ```
   
7. 지역번호가 02인 사람의 인원 수

   https://docs.djangoproject.com/en/3.2/ref/models/querysets/#startswith

   대소문자 구분 여부에 따라 `i `를 앞에 붙임

   - `ORM`: `__startswith` 

   ```python
   # orm
   
   In [47]: User.objects.filter(phone__startswith='02-').count()
   Out[47]: 24
   
   In [48]: print(User.objects.filter(phone__startswith='02-').query)
   SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user" WHERE "users_user"."phone" LIKE 02-% ESCAPE '\'
   ```

      ```sql
   -- sql
   
   sqlite> SELECT COUNT(*) FROM users_user
      ...> WHERE phone LIKE '02-%';
   COUNT(*)
   24
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   
   In [49]: User.objects.filter(country='강원도', last_name='황')
   Out[49]: <QuerySet [<User: User object (22)>]>
   
   In [50]: User.objects.filter(country='강원도', last_name='황').values()
   Out[50]: <QuerySet [{'id': 22, 'first_name': '은정', 'last_name': '황', 'age': 16, 'country': '강원도', 'phone': '016-5956-2725', 'balance': 7000}]>
   
   In [51]: User.objects.filter(country='강원도', last_name='황').values('first_name')  
   Out[51]: <QuerySet [{'first_name': '은정'}]>
   
   In [53]: User.objects.filter(country='강원도', last_name='황').values('first_name'). 
       ...: first()
   Out[53]: {'first_name': '은정'}
   
   In [54]: User.objects.filter(country='강원도', last_name='황').values('first_name'). 
       ...: first().get('first_name')
   Out[54]: '은정'
   ```

      ```sql
   -- sql
   
   sqlite> SELECT first_name FROM users_user
      ...> WHERE country = '강원도' AND last_name = '황';     
   first_name
   "은정"
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   https://docs.djangoproject.com/en/3.2/ref/models/querysets/#order-by

   ```python
   # orm
   
   In [55]: User.objects.order_by('-age')[:10].count()
   Out[55]: 10
   
   In [56]: User.objects.order_by('-age')[:10]
   Out[56]: <QuerySet [<User: User object (102)>, <User: User object (1)>, <User: User object (4)>, <User: User object (28)>, <User: User object (53)>, <User: User object (65)>, <User: User object (26)>, <User: User object (55)>, <User: User object (58)>, <User: User object (74)>]>
   
   In [57]: User.objects.order_by('-age')[:10].first().age
   Out[57]: 100
   
   In [58]: print(User.objects.order_by('-age')[:10].query)
   SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user" ORDER BY "users_user"."age" DESC LIMIT 10
   ```

      ```sql
   -- sql
   
   sqlite> SELECT * FROM users_user
      ...> ORDER BY age DESC LIMIT 10;
   id,first_name,last_name,age,country,phone,balance
   102,"길동","김",100,"경상북도",010-1234-1234,100
   1,"정호","유",40,"전라북도",016-7280-2855,370
   4,"미경","장",40,"충청남도",011-9079-4419,250000
   28,"성현","박",40,"경상남도",011-2884-6546,580000
   53,"상훈","홍",40,"전라북도",016-7698-6684,550
   65,"민서","송",40,"경기도",011-9812-5681,51000
   26,"영식","이",39,"경상북도",016-2645-6128,400000
   55,"미경","이",39,"경기도",02-6697-3997,890000
   58,"영일","배",39,"전라남도",010-3486-8085,280000
   74,"승민","배",39,"강원도",010-4833-9657,840
      ```

2. 잔액이 적은 사람순으로 10명

   - first & last

   https://docs.djangoproject.com/en/3.2/ref/models/querysets/#first

   https://docs.djangoproject.com/en/3.2/ref/models/querysets/#last

   ```python
   # orm
   
   In [59]: User.objects.order_by('balance')[:10]
   Out[59]: <QuerySet [<User: User object (102)>, <User: User object (99)>, <User: User 
   object (48)>, <User: User object (100)>, <User: User object (5)>, <User: User object 
   (24)>, <User: User object (61)>, <User: User object (92)>, <User: User object (46)>, 
   <User: User object (38)>]>
   
   In [60]: User.objects.order_by('balance')[:10].first().balance
   Out[60]: 100
   ```

      ```sql
   -- sql
   
   sqlite> SELECT * FROM users_user
      ...> ORDER BY balance LIMIT 10;
   id,first_name,last_name,age,country,phone,balance
   102,"길동","김",100,"경상북도",010-1234-1234,100
   99,"우진","성",32,"전라북도",010-7636-4368,150
   48,"보람","이",28,"강원도",02-2055-4138,210
   100,"재현","김",25,"경상북도",016-1252-2316,210
   ...
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명

   https://docs.djangoproject.com/en/3.2/ref/models/querysets/#union

   ```python
   # orm
   
   In [61]: User.objects.order_by('balance', '-age')[:10]
   Out[61]: <QuerySet [<User: User object (102)>, <User: User object (99)>, <User: User 
   object (48)>, <User: User object (100)>, <User: User object (5)>, <User: User object 
   (24)>, <User: User object (92)>, <User: User object (61)>, <User: User object (46)>, 
   <User: User object (38)>]>
   
   In [62]: print(User.objects.order_by('balance', '-age')[:10].query)
   SELECT "users_user"."id", "users_user"."first_name", "users_user"."last_name", "users_user"."age", "users_user"."country", "users_user"."phone", "users_user"."balance" FROM "users_user" ORDER BY "users_user"."balance" ASC, "users_user"."age" DESC LIMIT 10
   ```

   ```sql
   -- sql
   
   sqlite> SELECT * FROm users_user
      ...> ORDER BY balance ASC, age DESC LIMIT 10;
   id,first_name,last_name,age,country,phone,balance
   102,"길동","김",100,"경상북도",010-1234-1234,100
   99,"우진","성",32,"전라북도",010-7636-4368,150
   48,"보람","이",28,"강원도",02-2055-4138,210
   100,"재현","김",25,"경상북도",016-1252-2316,210
   ...
   ```

4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   In [63]: User.objects.order_by('-last_name', '-first_name')[4]
   Out[63]: <User: User object (67)>
   ```

      ```sql
   -- sql
   
   sqlite> SELECT * FROM users_user
      ...> ORDER BY last_name DESC, first_name DESC
      ...> LIMIT 1 OFFSET 4;
   id,first_name,last_name,age,country,phone,balance
   67,"보람","허",28,"충청북도",016-4392-9432,82000
      ```



---



### 4. 표현식

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#aggregate

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

   - (참고아래의 평균과 다른 이유는 이 작업 이후에 위에서 새로운 데이터 insertion을 진행하여 평균값이 변하기 때문)

   ```python
   # orm
   # shell_plus에서 자동으로 불러온다.
   In [64]: from django.db.models import Avg
       
   In [5]: User.objects.aggregate(Avg('age'))
   Out[5]: {'age__avg': 28.23}
   
   In [6]: User.objects.aggregate(age_value=Avg('age'))
   Out[6]: {'age_value': 28.23}
   ```

      ```sql
   -- sql
   
   sqlite> SELECT AVG(age) FROM users_user;
   AVG(age)
   28.23
      ```

2. 김씨의 평균 나이

   https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#generating-aggregates-over-a-queryset

   - 별명짓기

   ```python
   # orm
   
   In [66]: User.objects.filter(last_name='김').aggregate(Avg('age'))
   Out[66]: {'age__avg': 31.75}
   
   In [67]: User.objects.filter(last_name='김').aggregate(Avg('age')).get('age__avg')   
   Out[67]: 31.75
   
   In [68]: User.objects.filter(last_name='김').aggregate(age_avg_value=Avg('age'))     
   Out[68]: {'age_avg_value': 31.75}
   
   In [69]: User.objects.filter(last_name='김').aggregate(age_avg_value=Avg('age')).get 
       ...: ('age_avg_value')
   Out[69]: 31.75
   ```

      ```sql
   -- sql
   
   sqlite> SELECT AVG(age) FROM users_user
      ...> WHERE last_name = '김';
   AVG(age)
   31.75
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   
   In [71]: User.objects.filter(country='강원도').aggregate(Avg('balance'))
   Out[71]: {'balance__avg': 157895.0}
   
   In [72]: User.objects.filter(country='강원도').aggregate(Avg('balance')).get('balanc 
       ...: e__avg')
   Out[72]: 157895.0
   ```

   ```sql
   -- sql
   
   sqlite> SELECT AVG(balance) FROM users_user
      ...> WHERE country = '강원도';
   AVG(balance)
   157895.0
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   
   In [74]: User.objects.aggregate(Max('balance'))
   Out[74]: {'balance__max': 1000000}
   
   In [75]: User.objects.aggregate(Max('balance')).get('balance__max')
   Out[75]: 1000000
       
   # 가장 많은 잔고를 가진 사람 
   In [76]: user = User.objects.order_by('-balance').first()
   
   In [77]: user.last_name
   Out[77]: '김'
   
   In [78]: user.first_name
   Out[78]: '순옥'
   
   In [79]: user.balance
   Out[79]: 1000000
   ```

      ```sql
   -- sql
   
   sqlite> SELECT MAX(balance) FROM users_user;
   MAX(balance)
   1000000
   
   -- 가장 많은 잔고를 가진 사람 
   sqlite> SELECT * FROM users_user
      ...> ORDER BY balance DESC LIMIT 1;
   id,first_name,last_name,age,country,phone,balance
   70,"순옥","김",24,"제주특별자치도",016-4846-2896,1000000
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   
   In [80]: from django.db.models import Sum
   
   In [81]: User.objects.aggregate(Sum('balance'))
   Out[81]: {'balance__sum': 14425140}
   
   In [82]: User.objects.aggregate(Sum('balance')).get('balance__sum')
   Out[82]: 14425140
   ```

      ```sql
   -- sql
   
   sqlite> SELECT SUM(balance) FROM users_user;
   SUM(balance)
   14425140
      ```



## Annotate

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#annotate

지역별 인원수 

```python
# from django.db.models에 있는 Avg, Count, Min, Max, Sum은 Shell_plus에서 자동으로 import

In [83]: from django.db.models import Count

In [84]: User.objects.values('country')
Out[84]: <QuerySet [{'country': '전라북도'}, {'country': '경상남도'}, {'country': '전
라남도'}, {'country': '충청남도'}, {'country': '충청북도'}, {'country': '충청북도'}, 
{'country': '경기도'}, {'country': '충청북도'}, {'country': '제주특별자치도'}, {'country': '충청남도'}, {'country': '제주특별자치도'}, {'country': '충청남도'}, {'country': '전라북도'}, {'country': '전라남도'}, {'country': '경상북도'}, {'country': '경상남 
도'}, {'country': '충청남도'}, {'country': '충청북도'}, {'country': '충청남도'}, {'country': '경기도'}, '...(remaining elements truncated)...']>

In [85]: User.objects.values('country').annotate(Count('country'))
Out[85]: <QuerySet [{'country': '강원도', 'country__count': 14}, {'country': '경기도', 'country__count': 9}, {'country': '경상남도', 'country__count': 9}, {'country': '경
상북도', 'country__count': 16}, {'country': '전라남도', 'country__count': 10}, {'country': '전라북도', 'country__count': 11}, {'country': '제주특별자치도', 'country__count': 9}, {'country': '충청남도', 'country__count': 9}, {'country': '충청북도', 'country__count': 14}]>

In [86]: User.objects.values('country').annotate(my_countries=Count('country'))      
Out[86]: <QuerySet [{'country': '강원도', 'my_countries': 14}, {'country': '경기도', 
'my_countries': 9}, {'country': '경상남도', 'my_countries': 9}, {'country': '경상북도
', 'my_countries': 16}, {'country': '전라남도', 'my_countries': 10}, {'country': '전 
라북도', 'my_countries': 11}, {'country': '제주특별자치도', 'my_countries': 9}, {'country': '충청남도', 'my_countries': 9}, {'country': '충청북도', 'my_countries': 14}]> 

In [87]: User.objects.values('country').annotate(my_countries=Count('country')).firs 
    ...: t()
Out[87]: {'country': '전라북도', 'my_countries': 1}

In [88]: User.objects.values('country').annotate(my_countries=Count('country')).firs 
    ...: t().get('my_countries')
Out[88]: 1
                                                             
In [89]: User.objects.values('country').annotate(Count('country'), avg_balance=Avg(' 
    ...: balance'))
Out[89]: <QuerySet [{'country': '강원도', 'country__count': 14, 'avg_balance': 157895.0}, {'country': '경기도', 'country__count': 9, 'avg_balance': 182852.22222222222}, {'country': '경상남도', 'country__count': 9, 'avg_balance': 73870.0}, {'country': '경 
상북도', 'country__count': 16, 'avg_balance': 70909.375}, {'country': '전라남도', 'country__count': 10, 'avg_balance': 66265.0}, {'country': '전라북도', 'country__count': 11, 'avg_balance': 161138.18181818182}, {'country': '제주특별자치도', 'country__count': 9, 'avg_balance': 351233.3333333333}, {'country': '충청남도', 'country__count': 9, 'avg_balance': 104304.44444444444}, {'country': '충청북도', 'country__count': 14, 'avg_balance': 159610.7142857143}]>
```

