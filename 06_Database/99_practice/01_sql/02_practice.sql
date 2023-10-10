-- library.db 파일을 생성하여 데이터베이스로 사용한다.
-- sql 파일을 생성하고 각 요구 사항을 만족하는 코드를 작성하고 실행 결과를 확인하시오.


-- Authors 테이블을 생성한다. 상세한 schema는 첨부 파일 참고.
CREATE TABLE Authors (
  author_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(100) NOT NULL,
  nationality VARCHAR(100) NOT NULL
);

-- Books테이블을 생성한다. 상세한 schema는 첨부 파일 참고.
CREATE TABLE Books (
  book_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  pub_year INTEGER NOT NULL,
  author_id INTEGER NOT NULL,
  FOREIGN KEY (author_id)
    REFERENCES Authors(author_id)
);

-- Authors 테이블에 서로 다른 데이터를 최소 3개 이상 삽입한다.
INSERT INTO
  Authors (name, nationality)
VALUES
  ('강성은', '한국'),
  ('정지헌', '일본'),
  ('한성주', '제주도'),

-- Books 테이블에 서로 다른 데이터를 최소 3개 이상 삽입한다.


-- Authors 테이블의 모든 데이터 조회한다.

-- Books 테이블의 모든 데이터 조회한다. 단, 관계 맺고 있는 Authors 테이블의 name도 함께 출력한다.

-- Authors 테이블의 1번째 레코드의 nationality를 '스코틀랜드'로 수정한다.

-- Authors 테이블에 새로운 레코드를 추가한다. 
  -- name : 'F. 스콧 피츠제럴드'
  -- nationality: '미국'

-- Books 테이블에 새로운 책을 추가한다. 저자는 'F. 스콧 피츠제럴드' 으로 작성한다.

-- Books 테이블 정보를 수정한다.
  -- publication_year 열의 이름을 '출판년도'로 수정한다.

-- Authors 테이블에서 '하퍼 리'의 레코드 삭제한다.

-- Books 테이블에서 저자가 없는 레코드만 삭제한다.

-- Authors와 Books 의 모든 데이터를 조회한다.