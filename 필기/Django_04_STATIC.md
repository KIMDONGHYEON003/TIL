# Django_04_STATIC



### Static files

- 정적 파일
- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  - 사용자의 요청에 따라 내용이 바귀는 것이 아니라 요청한 것을 그대로 보여주는 파일
- 웹사이트는 일반적으로 이미지, 자바스크립트 또는 css와 같은 미리 추가된 추가 파일을 제공해야함
- django에서는이러한 파일을 static file이라고 함



- 구성

  - django.contrib.staticfiles가 INSTALLED_APPS에 포함되어 있는지 확인

  - settings.py에서 STATIC_URL을 정의

  - 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 필드

    ```python
    {% load static %}
    <img src="{% static 'my_app/example.jpg' %}" alt = "My image">
    ```

  - 앱의 static 폴더에 정적파일을 저장

- load

  - 사용자 정의 탬플릿 태그 세트를 로드
  - 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 로드

- static

  - STATIC_ROOT 에  저장된 정적 파일에 연결

    ```python
    {% load static %}
    <img src="{% static 'my_app/example.jpg' %}" alt = "My image">
    ```

    

  - STATIC_ROOT

    - collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로	```$ python manage.py collectstatic```
    - django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로
    - 개발 과정에서 setting.py의 DEBUG값이 True로 설정되어 있으면 해당 값은 작용되지 않음
      - 직접 작성하지 않으면 django 프로젝트에서는 setting.py에 작성되어 있지 않음
    - 실 서비스 환경(배포 환경)에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함

    

  - STATIC_URL

    - STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
      - 개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로(기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 참색함
    - 실제 파일이나 디렉토리가 아니며, URL로만 존재
    - 비어있지 않은 값으로 설정한다면 만드시 slash(/)로 끝나야 함
    - 

  - STATICFILES_DIRS

    - app/static/디렉토리 경로를 사용하는 것 욍에 추가적인 정적 파일 경로 목록을 정의하는 리스트
    - 추가 파일디렉토리에 대한 전체 경로를 포함하는 문자열 목록을 작성되어야 함



- 이미지 업로드
  - 미디어 파일
  - 사용자가 웹에서 업로드하는 정적 파일
  - 유저가 업로드한 모든 정적 파일
  - ImageField
    - 이미지 업로드에 사용하는 모델 필드
    - FileField를 상속 받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능
    - 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사함
    - ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경할 수 있음
    - Pillow 라이브러리가 필요
    - upload_to = 'images/'
      - 실제 이미지가 저장되는 경로를 지정
    - blank = True
      - -이미지 필드에 빈 값이 허용되도록 설정(이미지를 선택적으로 업로드할 수 있도록)
  - FileField
    - 파일 업로드에 사용하는 모델 필드
    - 2개의 선택인자를 가지고 있음
      - upload_to - 이것만 확인
      - storage
  - MEDIA_ROOT
    - 사용자가 업로드한 파일들을 보관할 디렉토리의 절대 경로
    - django는 성능을 위해 업로드 파일은 디비에 저장하지 않음
      - 실제 디비에 저자오디는 것은 파일의 경로
    - **MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야함**
    - MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
    - SLASH로 끝나야한다
  - model field option = "null"
    - 기본값 : false
    - true면 django는 빈 값을 db에 null로 저장
    - 주의사항
      - charfield, textfield와 같은 문자열 기반 필드에는 사용하는 것을 피해야함
      - 문자열 기반 필드에 true로 설정시 데이터 없음 에 빈문자열과 null의 2가지 가능한 값이 있음을 의미하게 됨
      - 대부분의 경우 데이터 없음에 대해 두개의 가능한 값을 갖는 것은 중복되며, django는 null이 아닌 빈 문자열을 사용하는 것이 규칙
    - blank
      - validation-related
    - null
      - database-related
    - 문자열 기반 및 비문자열 기반 필드 모두에 대해 null option은 db에만 영향을 미치므로, form에서 빈 값을 허용하려면 blank=True를 설장해야 함