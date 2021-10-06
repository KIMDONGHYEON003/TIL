/*
1. SQL은 ;까지 하나의 명령어(Query)로 간주.
2. .은 sqlite3 프로그램의 기능이 실행하는 것 (SQL문이 아님)
3. 테이블은 여러 개 있어도 된다. 
4. SQL 명령어는 소문자로 써도 동작하지만 대문자를 권장한다.
5. rowid는 PRIMARY KEY 속성 컬럼을 작성하지 않으면 값이 자동으로 증가하는 옵션을 가진 컬럼
    - INTEGER PRIMARY KEY 타입으로 컬럼 생성시 rowid 대체
    - PK는 INTEGER에서만 사용가능
    - rowid 컬럼은 직접 값을 넣어주지 않아도 알아서 증가하지만 id 컬럼을 지정하는 순간 값을 넣어 주지 않으면 INSERT 불가
6. 
*/

-- DB 생성 
-- 있으면 접속 없으면 생성
sqlite3 tutorial.sqlite3

-- (참고) 
-- 앞에 .이 붙는 명령어는 SQL문이 아니라 sqlite3라는 프로그램의 명령어
-- SQL문은 항상 ;으로 끝난다.
.databases

-- csv 파일을 불러와서 db 저장
.mode csv 
.import hellodb.csv examples

-- 추가 설정
.headers on
.mode column

-- 테이블 확인
.tables

-- 조회 (READ)
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232

-- TABLE 생성
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );

  
-- TABLE 조회 및 Schema 조회
sqlite> .tables
classmates  examples

sqlite> .schema classmates
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

-- TABLE 삭제
sqlite> DROP TABLE classmates;
sqlite> .tables
examples

-- Data 추가(INSERT) - CREATE
sqlite> INSERT INTO classmates (name, age)
   ...> VALUES ('홍길동', 23);

-- 모든 열에 데이터를 넣을 때는 column 명시 필요 x
sqlite> INSERT INTO classmates VALUES ('홍길동', 30, 
'서울');

-- TABLE 다시 만들기
sqlite> DROP TABLE classmates;
sqlite> .tables
examples
sqlite> CREATE TABLE classmates(
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );

-- 
sqlite> INSERT INTO classmates (name, age)
   ...> VALUES ('홍길동', 23);
-- Error: NOT NULL constraint failed: classmates.address

sqlite> INSERT INTO classmates VALUES ('홍길동', 30, '서울'); 
-- Error: table classmates has 4 columns but 3 values were supplied

-- 2가지 방법으로 데이터를 넣자
--1. 
sqlite> INSERT INTO classmates (name, age, address) VALUES (' 
김영희', 11, '대전');

--2. 
sqlite> INSERT INTO classmates VALUES (2, '홍길동', 30, '서울');
sqlite> SELECT * FROM classmates;
id  name  age  address
--  ----  ---  -------
1   김영희   11   대전
2   홍길동   30   서울


-- 다시 만들자!
sqlite> DROP TABLE classmates;
sqlite> .tables
examples
sqlite> CREATE TABLE classmates(
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
sqlite> INSERT INTO classmates VALUES ('홍길동', 30, '서울'), 
('김철수', 23, '대전'), ('박나래', 23, '광주'), ('이요셉', 33 ('김철수', 23, '대전'), ('박나래', 23, '광주'), ('이요셉', 33, '구미');
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   30   서울
김철수   23   대전
박나래   23   광주
이요셉   33   구미
sqlite> SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   30   서울
2      김철수   23   대전
3      박나래   23   광주
4      이요셉   33   구미

-- rowid, name만 가져오기
sqlite> SELECT rowid, name FROM classmates;
rowid  name
-----  ----
1      홍길동
2      김철수
3      박나래
4      이요셉

-- LIMIT
sqlite> SELECT rowid, name FROM classmates LIMIT 1;
rowid  name
-----  ----
1      홍길동

-- LIMIT & OFFSET
sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;  
rowid  name
-----  ----
3      박나래

-- WHERE
sqlite> SELECT rowid, name FROM classmates WHERE address='서울
';
rowid  name
-----  ----
1      홍길동
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   30   서울
김철수   23   대전
박나래   23   광주
이요셉   33   구미

-- DISTINCT
sqlite> SELECT DISTINCT age FROM classmates;
age
---
30
23
33

-- DELETE - CRUD 중 D
sqlite> DELETE FROM classmates WHERE rowid=4;
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   30   서울
김철수   23   대전
박나래   23   광주
sqlite> SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   30   서울
2      김철수   23   대전
3      박나래   23   광주


-- AUTOINCREMENT
/*
sqlite> CREATE TABLE tests (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> name TEXT NOT NULL);
sqlite> .tables
classmates  examples    tests
sqlite> INSERT INTO tests (name) VALUES ('홍길동'), ('김철수' sqlite> INSERT INTO tests (name) VALUES ('홍길동'), ('김철수');

sqlite> SELECT * FROM tests;
id  name
--  ----
1   홍길동
2   김철수
sqlite> DELETE FROM tests WHERE id=2;
sqlite> SELECT * FROM tests;
id  name
--  ----
1   홍길동
sqlite> sqli

sqlite> INSERT INTO tests (name) VALUES ('최철순');
sqlite> SELECT * FROM tests;
id  name
--  ----
1   홍길동
3   최철순

*/

-- UPDATE - CRUD U
sqlite> UPDATE classmates
   ...> SET name='홍길동', address='제주도'
   ...> WHERE rowid=4;
sqlite> SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   30   서울
2      김철수   23   대전
3      박나래   23   광주
4      홍길동   45   제주도

-- WHERE 문 심화
sqlite> SELECT * FROM users WHERE age >= 30;
sqlite> SELECT first_name FROM users WHERE age >= 30;
sqlite> SELECT first_name, age FROM users WHERE age >= 30 and 
last_name = '김';

-- Expression
sqlite> SELECT COUNT(*) FROM users;
COUNT(*)
1000
sqlite> SELECT AVG(age) FROM users WHERE age >= 30;
AVG(age)
35.1763285024155
sqlite> SELECT first_name, MAX(balance) FROM users;
first_name,MAX(balance)
"선영",990000

-- LIKE 
sqlite> SELECT * FROM users WHERE age LIKE '2_';
sqlite> SELECT * FROM users WHERE phone LIKE '02-%';
sqlite> SELECT * FROM users WHERE first_name LIKE '%준'; 
sqlite> SELECT * FROM users WHERE phone LIKE '%-5114-%';

-- ORDER
-- users에서 나이순으로
-- 오름차순 정렬하여 상위 10개만 뽑아보면?
id|first_name|last_name|age|country|phone|balance
240|현준|황|37|충청북도|011-5114-9343|220

sqlite> SELECT * FROM users ORDER BY age LIMIT 10;
sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;
id|first_name|last_name|age|country|phone|balance
11|서영|김|15|제주특별자치도|016-3046-9822|640000
59|지후|엄|15|경상북도|02-6714-5416|16000
61|우진|고|15|경상북도|011-3124-1126|300
125|우진|한|15|강원도|011-8068-4814|3300
144|은영|이|15|전라남도|010-5284-4904|78000
196|지훈|김|15|전라북도|02-9385-7954|760
223|승현|장|15|충청북도|016-5731-8009|450
260|주원|김|15|전라남도|02-4240-8648|6300
294|은정|이|15|경상북도|010-6099-6176|5900
295|정수|강|15|충청북도|02-7245-5623|500

-- ASC는 생략 가능(기본값)
sqlite> SELECT * FROM users ORDER BY age ASC, last_name ASC LIMIT 10;
sqlite> SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

-- GROUP BY 

sqlite> SELECT last_name, COUNT(*)
   ...> FROM users
   ...> GROUP BY last_name;

sqlite> SELECT last_name, COUNT(*) AS name_count
  ...> FROM users
  ...> GROUP BY last_name;

sqlite> SELECT last_name, COUNT(*) AS name_count
   ...> FROM users
   ...> GROUP BY last_name
   ...> ORDER BY name_count DESC;

-- ALTER
sqlite> CREATE TABLE articles (
   ...> title TEXT NOT NULL,
   ...> content TEXT NOT NULL
   ...> );
sqlite> .tables
articles    classmates  examples    tests       users
sqlite> INSERT INTO articles VALUES ('1번제목', '1번내용');


sqlite> ALTER TABLE articles
   ...> RENAME TO news;
sqlite> .tables
classmates  examples    news        tests       users

sqlite> ALTER TABLE news
   ...> ADD COLUMN created_at TEXT NOT NULL;
Error: Cannot add a NOT NULL column with


--1. NOT NULL 제외
sqlite> ALTER TABLE news
   ...> ADD COLUMN created_at TEXT;
sqlite> INSERT INTO news
   ...> VALUES ('title', 'content', datetime('now'));
sqlite> SELECT * FROM news;
title|content|created_at
1번제목|1번내용|
title|content|2021-09-14 20:52:12|1

--2. DEFAULT VALUE 
sqlite> ALTER TABLE news
   ...> ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;

sqlite> SELECT * FROM news;
title|content|created_at|subtitle
1번제목|1번내용||1
title|content|2021-09-14 20:55:12|1