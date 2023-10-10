DROP TABLE articles;

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('제목', '내용', '2000-01-01');

SELECT rowid, * FROM articles;

SELECT * FROM articles;

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('제목2', '내용2', '2000-01-11'),
  ('제목3', '내용3', '2000-01-11'),
  ('제목4', '내용4', '2000-01-11');

INSERT INTO articles
  (title, content, createdAt)
VALUES
  ('제목5', '내용5', '2000-01-11');

-- 테이블이 가진 모든 데이터 삭제
-- DELETE FROM articles;

-- 5번 게시글만 삭제
DELETE FROM 
  articles
WHERE 
  rowid = 5;

INSERT INTO articles
  (rowid, title, content, createdAt)
VALUES
  (2, '제목1', '내용1', '2000-01-11');

UPDATE articles
SET title = '수정'
WHERE id = 1;

UPDATE articles
SET title = '2번',
    content = '수정'
WHERE id = 2;

DELETE FROM articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);