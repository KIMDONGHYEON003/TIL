# Django 03



- Form Class

  - model을 선언하는 것과 유사하며 같은 필드 타입을 사용

  -  forms 라이브러리에서 파생된 Form 클래스를 상속받음

  - as_p()

    - 각 필드가 단락으로 감싸져서 렌더링

  - as_ul()

    - 각 필드가 목록 항목으로 감싸
    - ul 태그는 직접 작성해야함

  - as_table()

    - 각 필드가 테이블 행으로 감싸져서 렌더링
    - table 태그는 직접 작성해야함

  - Form fields

    - input에 대한 유효성 검사 로직을 처리하며 템플리셍서 직접 사용됨

  - Widgets

    - 웹 페이지의 HTML input요소 렌더링
    - GET / POST 딕셔너리에서 데이터 추출
    - 하지만 widgets은 반드시 form fields 에 할당됨

    - django 의 html input element 표
    - 주의사항
      - form fields 와 혼동 되어서는 안됨
      - form fields input 유효성 검사를 처리
      - widgets은 웹 페이지에서 input element 의 단순한