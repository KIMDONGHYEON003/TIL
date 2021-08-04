# 02 web

## css layout

1. Float - 둥둥 뜨다?

   - 한 요소가 정상 흐름으로부터 빠져나와 **텍스트 및 인라인 요소**가 그 주위를 감싸 요소의 좌, 우측을 따라 배치되어야 함을 지정

   - 본래는 이미지를 한쪽으로 띄우고 텍스트를 둘러싸는 레이어웃을 위해 도입

   - 더 나아가 이미지가 아닌 다른 요소들에도 적용해 웹 사이트의 전체 레이아웃을 만드는데까지 발전

   - 신문 구조 float left / float right

     

   - none : 기본값 // left :요소를 왼쪽으로 띄움 // right:요소를 오른쪽으로 띄움

     

   - Float clear : clear fix - 부모를 만든 후 부모 태그에 css를 넣는다

     - 선택한 요소의 맨 마자막 자식으로 가상 요소를 하나 생성
     - 보통 content 속성과 함게ㅐ 장식용 콘텐츠를 추가할 대 사용
     - 기본값은 inline 그래서 ```display: block;``` 추가적으로 함
     - 선행 요소가 float가 됐으면 해제하는 의미 ```clear: both;```

     ```html
     .clearfix::after{      /* 의사요소  가상요소 */
           content: "";
           display: block;
           clear: both;     /*보통은 both를 사용*/
         }
     ```

     가장 일반적인 예시

     블록 요소인 가상의 공간을 만들어서 아랫 쪽의 것들이 위로 못 올라오게 만든다

     clear를 안주면 가상의 요소 또한 float 아래쪽으로 들어갈 수 있다.

     float가 됐다는 사실을 무시해야한다.

     

   - ::은 무엇인가? : 선택한 요소의 맨 마지막 자식으로 의사(가상) 요소를 하나 생성한다. / 기본값은 인라인

     mdm참고

     

   - flexbox 및 grid 레이아웃과 같은 기술이 나오기 이전에 float은 열 레이아수을 만드는데 사용됨

   - flexbox와 grid의 출현과 함께 원래 텍스트 블록 내에서 float 이미지를 위한 역할로 돌아감

     - mdn 에서는 더 새롭고 나은 레이아웃 기술이 나와있으므로 "legacy레이아웃 기술" 로 분류

   - 웹에서 여전히 사용하는 경우도 있음 (ex. naver의 nav bar)

     - ```css
       #gnb .list_nav {
           float: left;
           font-size: 15px;
           line-height: 30px;
           font-weight: 700;
           color: #000;
           letter-spacing: -.3px;
       }
       ```







2. Flex Box (CSS Flexible Box Layout) - 가장 처음 해야하는 것 : flex container 선언

   - 오랫동안 CSS Layout을 작성할 수 있는 도구는 float 및 positioning 뿐이었음

     - 문제가 있는 것은 아니지만 어떤 면에서는 제한적이고 한계가 있음

   - flexbox라 불리는 flexbox 인터페이스 내의 아이템 간 **공간배분** **정렬** 기능을 제공하기 위한 1차원 레이아웃 모델로 설계

   - 요소 간 공간 배분과 정렬 기능을 위한 1차원(단방향) 레이아웃

   - **요소** **축**

   - 요소

     - flex container (부모요소)
     - flex item(자식요소)

   - 축

     - main axis(메인 축) - 꼭 x 축은 아니다 결정하기에 따라 다름
     - cross axis(교차 축)

   - flex container (부모요소)

     - flxbox 레이아웃을 형성하는 가장 기본적인 모델
     - flex item 들이 놓여있는 영역
     - 생성하려면 display 속성을 flex 혹은 inline- fex 로 지정

   - flex item(자식 요소)

     - 컨테이너의 컨텐츠

       

   - 배치 방향 설정 : flex-direction (상하좌우 4방향)

   - 메인축 방향 설정 :**justify**-content

     - 메인축 방향만 바뀐다
     - flexbox는 단방향 레이아웃이기 때문
     - row(default) / row-reverse / column / column-reverse

   - 교차축 방향 정렬 :  교차축은 고민할 필요 없음 메인축 기준으로 교차축이 결정되기 때문

     - **align**-items
     - **align**-self
     - **align**-content

   - 기타 flex-wrap

     

   - content : 여러 줄

   - items : **한줄**

   - self :flex item 개별 요소

   - ex)

     - justify-content : 메인축 기준 여러 줄 정렬
     - align-items : 교차축 기준 한 줄 정렬
     - align-self : 교차축 기준 선택한 요소 하나 정렬

   - ```css
         .flex-container{
           /* 1. 정렬하고자 하는 부모 요소(flex contatiner)에 선언 */
           display: flex;
     
           /* display: inline-flex; */
           /* ㄴ 안에 있는 요소 만큼만 차지 */
           
           /*2. 메인축 방향 설정*/
           /*flex-direction: row; default 설정*/
           /*flex-direction: row-reverse; /efault 값과 반대 방향*/
           /*flex-direction: column; 위에서 아래로 교차축 만큼 사이즈가 꽉참*/
           /*flex-direction: column-reverse; 아래에서 위로 방향이 결정*/
           
           /*3. item들이 강제로 한 줄에 배치되게 할 것인지에 대한 여부 결정*/
           /* flex-wrap: nowrap; */
           /*wrap 없음*/
           /* flex-wrap: wrap; */
           /*wrap을 쓰면 초과된 태그가 밖으로 나가지 않고 아래로 내려간다*/
           /* flex-wrap: wrap-reverse; */
           /*wrap-reverse을 쓰면 초과된 태그가 밖으로 나가지 않고 윗줄로 올라간다*/
     
           /*4. flex-direction + flex-wrap의 shorthand*/
           /* flex-flow: column-reverse wrap; */
           /*ㄴ 함께 쓸 수 있다*/
           
           /*5. 메인축 정렬*/
           justify-content: flex-start;
           /*ㄴ 기본값 default*/
           /* justify-content: center; */
           /*ㄴ 가운데*/
           /* justify-content: flex-end; */
           /* ㄴ오른쪽 끝으로 붙는다.*/
           /* justify-content: space-between; */
           /* ㄴ골고루 배치된다 / 좌우 정렬 / 아이템간 간격이 동일*/
           /* justify-content: space-around; */
           /* ㄴ 균등 좌우 정렬 / 내부 간격이 외부 요소의 두배이다*/
           /* justify-content: space-evenly; */
           /*  ㄴ균등 정렬 / 내부 간격 외부 간격이 동일*/
     
           /*6. 교차축 정렬*/
           /* align-items: stretch; */
           /*ㄴ 기본값*/
           /* align-items: flex-start; */
           /* align-items: center; */
           /*ㄴ교차축 기준 가운데 정렬*/
           /* align-items: flex-end; */
           /*ㄴ 교차축 기중 마지막 정렬*/
           /* align-items: baseline; */
     
         }
         /*7. 교차축 개별 정렬*/
         .item1{
     
           /* align-self: flex-start; */
     
           /*order  값이 작을수록 앞으로 정렬 (기본값 0)*/
           /* order: 0; */
           /* 기본값이 0이다.*/
           order: 0;
     
           /* 메인축에서 남은 공간을 개수만큼 각 항목에게 분배*/
           /*남은 공간에 대한 배분*/
           /* 기본값이 0이다.*/
           flex-grow: 1;
         }
     
         .item2{
           /* align-self: center; */
           /* order: -1; */
           /*2번 박스가 맨 앞으로 맨 좌측으로간다.*/
     
           
           flex-grow: 2;
         }
           
         .item3{
           /* align-self: flex-end; */
           /* order: 1; */
           /*메인 축 기준으로 가장 끝으로 간다*/
     
           flex-grow: 3;
         }
     ```

     정렬의 주체는 부모

     하지만 self는 정렬의 주체가 자식