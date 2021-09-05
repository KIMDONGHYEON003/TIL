# Django 정리

- Model 정리
  - 웹 앱의 데이터를 구조화하고 조작하기 위한 도구



- ### ORM

  - Object Relational Mapping
  - 객체 지향 프로그래밍을 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환
  - Django는 내장 Django ORM을 사용함
  - 장점
    - sql을 잘 알지 못해도 조작 가능
    - 절차적 접근이 아닌 객체 지향적 접근으로 높은 생산성
  - 단점
    - orm 만으로 완전한 서비스를 구현하기는 어려움
  - 현대 웹 프레임 워크의 요점은 웹 개바르이 속도를 높이는 것 (**생산성**)

  - models.py를 작성

  - ```python
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
    ```

  - 모델 필드

    - CharField(max_length=None, **options)
      - 길이 제한이 있는 문자열을 넣을 때 사용
      - max_length는 필수 인자
    - TextField(**options)
      - 글자 수가 많을 때 사용
      - max_length 옵션 작성시 자동 양식 필드인 textarea위젯에 반영은 되지만 모델과 데이터베이스 수준에는 적용되지 않음

- ### Migrations

  - django가 model에 생긴 변화를 반영하는 방법

  - **python manage.py makemigrations**

    - 모델을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용

  - **python manage.py migrate**

    - 마이그레이션을 db에 반영하기 위함
    - 설계도를 실제 db에 반영하는 과정

  - **python manage.py sqlmigrate (appname) (0001)**

    - 마이그레이션에 대한 sql 구문을 보기 위해 사용
    - 마이그레이션이 sql문으로 어떻게 해석되
    - 
    - 어서 동작할지 미리 확인 가능

  - **python manage.py showmigrations**

    - 프로젝트 전체의 마이그레이션 상태를 확인하기 위함
    - 마이그레이션 여부를 확인할 수 있음

  - ex) 추가 모델 필드 작성 후 makemigrations진행

  - **auto_now_add** : 최초 생성 일자 - 최초 insert시에만 현재 날짜와 시간으로 갱신

  - **auto_now** : 최종 수정 일자 orm이 save 할 때마다 현재 날짜와 시간으로 갱신

  - ##### Migration 3단계

    1. models.py : model 변경사항 발생 시
    2. $ python manage.py makemigrations : migrations 파일 생성
    3. $ python manage.py migrate : db 반영 / 모델과 db의 동기화



- ### DB API

  - (class name).(manager).all()
  - Article.objects.all()
  - Manager
    - django 모델에 데이터베이스 쿼리 작업이 제공되는 인터페이스
    - 기본적으로 모든 django 모델 클래스에 objects라는 manager를 추가
  - QuerySet
    - 데이터베이스로부터 전달받은 객체 목록
    - queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
    - 데이터 베이스로부터 조회, 필터, 정렬 등을 수행할 수 있음
  - Django shell
    - 일반 python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음
    - Django-extensions 라이브러리 기능 중 하나를 사용한다.
    - ```$ pip install ipython```
    - ``` $ pip install django-extensions```
    - **라이브러리 설치 후에 ```settings.py```파일로 이동해서 ```INSTALLED_APPS```에 추가해야함**
    - **``` $ python manage.py shell_plus``` : shell_plus 실행 명령어**

- ### CRUD

  - CREATE // READ // UPDATE // DELETE

  - 기본적인 데이터 처리 기능

  - ```Article.objects.all()``` : 전체 article 객체 조회

  - ```article = Article()``` : 

  - ```article.title = 'first'``` : 인스턴스 변수 title에 값을 할당

  - ```article.content = 'django'``` : 인스턴스 변수  content에 값을 할당

  - 여기서 save를 하지 않으면 db에 값이 저장되지 않음

  - ```article.save()``` : 저장

  - ```article.title```: 해당 명령어를 치면 title 값을 불러낼 수 있다.

  - ``` article = Article(title='second', content='django!!')``` : 해당 명령어로도 인스턴스 변수에 값을 할당할 수 있음

  - ```article.pk```

  - ```Article.objects.create(title='third', content='django!' )``` : 해당 명령어로도 인스턴스 변수에 값을 할당할 수 있음

  - 

  - ```python
    class Article(models.Model):
        title = models.CharField(max_length = 10)
        content = models.TextField()
        
        def __str__(self):
            return self.title
        
    # str 클래스 메소드로
    # 각각의 object가 사람이 읽을 수 있는 문자열을 반환하도록 할 수 있음
    ##### 작성후 반드시 shell_plus를 재시작해야 반영됨
    ```

  - query set

    - all() : 복사본을 반환
    - get() 
      - 주어진 lookup 매개변수와 일치하는 객체를 반환
      - 객체를 찾을 수 없으면 **DoesNotExist** 예외를 발생
      - 둘 이상의 객체를 찾으면 **MultipleObjectReturned** 예외를 발생
      - **primary key와 같이 고유성을 보장하는 조회에서 사용해야함**
    - filter() : 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 queryset을 반환
    - .delete() 
      -  queryset의 모든 행에 대해 sql 삭제 쿼리를 수행
      - 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환
      - ```(, {'articles.Article' : 1})``` 이런 식으로 반환됨



- ### Admin Site

  - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지

  - Model class를 **admin.py**에 등록하고 관리

  - **django.contrib.auth** 모듈에서 제공됨

  - record 생성 여부 확인에 매우 유용하며, 직점 record를 삽입할 수도 있음

  - 

  - ##### admin 생성

    - ```$ python manage.py createsuperuser``` 
      - 관리자 계정 생성 후 서버를 실행한 다음 '/admin'으로 가서 관리자 페이지 로그인
      - 계정만 만든 경우 django 관리자 화면에서 아무 것도 보이지 않음
      - 내가 만든 record를 보기 위해서는 admin.py에 작성하여 djnago 서버에 등록
      - 주의 : auth에 관련된 기본 테이블이 생성되지 않으면 관리자 계정을 생성할 수 없음

  - ##### admin 등록

    - ```python
      from djnago.contrib import admin
      from .models import Article
      
      class ArticleAdmin(admin.ModelAdmin):
          list_display = ('pk','title','content','created_at','updated_at')
      ### models.py 정의한 각각의 속성들의 값을 admin 페이지에 출력하도록 설정
      
      admin.site.register(Article)
      
      ### admin.py는 관리자 사이트에 Article 객체가 관리자 인터페이스를 가지고 있다는 것을 알려주는 것
      ### models.py 에 정의한 __str__의 형태로 객체가 표현됨
      ```





- ### CRUD 해보기

  - ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR/'templates'], ## 다음과 같이 지정해야 base.html을 사용할 수 있다.
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

  - ``` 'DIRS': [BASE_DIR/'templates'], ## 다음과 같이 지정해야 base.html을 사용할 수 있다.```





- - HTTP method

    - GET
      - 특정 리소스를 가져오도록 요청할 때 사용
      - 반드시 데이터를 가져올 때만 사용해야함
      - DB에 변화를 주지 않음
      - CRUD에서 READ 역할을 담당
    - POST
      - 서버로 데이터를 전송할 때 사용
      - 데이터를 HTTP BODY에 담아 전성
      - 서버에 변경사항을 만듦
      - CRUD에서 CREATE UPDATE DELETE 역할을 담당

    

  - 사이트 간 요청 위조(Cross-site request forgery)

    - 웹 앱 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 한다거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
    - django는 CSRF에 대항하여 **middleware**와 **template tag**를 제공
    - CSRF라고도 함

    

  - CSRF 공격 방어

    - Security Token 사용 방식

      - 사용자의 데이터에 임의의 난수 값을 부여해, 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함
      - 이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증

    - 일반적으로 데이터 변경이 가능한 post, patch, delete method 등에 적용 **(GET 제외)**

    - Django는 **token 템플릿 태그**를 제공

      - ```{% csrf_token %}```

      - input type이 hidden으로 작성 value는 django에서 생성한 hash값으로 설정

      - 해당 태그 없이 요청을 보내면 **403 forbidden**

      - csrf 공격 관련 보안 설정은 ```settings.py```에서 **MIDDLEWARE**에 작성되있음

        - 실제로 요청 과정에서 ```urls.py```이전에 MIDDLEWARE의 설정 사항들을 **순차적**으로 거치며 **응답은 반대로 하단에서 상단**으로 미들웨어를 적용시킴

        

  - **Redirect**

    - 새 url로 되돌림
    - 인자에 따라 **HttpResponseRedirect**를 반환
    - 브라우저는 현재 경로에 따라 전체 url 자체를 재구성
    - 사용 가능 인자
      - model
      - view name
      - absolute or relative URL

  - ##### Variable Routing

    - 게시판에 주로 사용

    - ```<int:pk>``` 을 urls.py의 url로 사용

    - ```python
      def edit(request, movie_pk):
          movie = Movie.objects.get(pk=movie_pk)
          # pk중 왼쪽 pk는 DB에 저장된 레코드의 PK
          context = {
              'movie': movie,
          }
          return render(request, 'movies/edit.html', context)
      ```

    - ```python
      <a href ="{% url 'movies:edit' movie.pk %}" class="mx-1">
      
      # 특정 pk를 edit 해야하기 때문에 edit 버튼에 pk 값을 넣어준다.
      ```

    - 





- ##### Model

  - 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구

- ##### Database

  - 체계화된 데이터의 모임

- ##### Migrations

  - django가 model에 생긴 변화를 반영하는 방법

- ##### ORM

  - OOP 언어를 사용하여 데이터 베이스와 OOP 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- ##### Database API

  - DB를 조작하기 위한 도구()

- Admin Site

  - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지







##### MTV

- M(odel) / M
  - 데이터베이스와 통신(관리)
  - 데이터의 구조 설정
  - 데이터베이스의 기록을 관리(CRUD)
- T(emplate) / V
  - 화면 (레이아웃)
  - 사용자에게 실제 내용을 보여주는 것(presentation)
- V(iew) / C
  - 중간관리자
  - Client의 요청에 맞는 view 내부의 함수가 실행되는 Model & Template을 정의하여 응답을 반환한다.
  - 



action?

- form을 입력받고 해당 데이터를 서버로 전송할 때 보낼 경로가 들어가는 속성값





```  path('<int:movie_pk>/', views.detail, name='detail' ),```

