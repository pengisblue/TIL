# 10/11 강의
## 개요
### Many to one relationships
> N:1 or 1:N
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
### Comment(N)-Article(1)
- 0개 이상의 댓글은 1개의 게시 글에 작성될 수 있다.
- 테이블 관계
    - Comment - Article에 대한 외래 키(ForeignKey())

## 댓글 모델 구현
### ForeignKey(to, on_delete)
- to : 참조하는 객체(class)
- on_delete : 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)
    - 'CASCADE' : 참조 된 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제

## 댓글 생성 연습
```shell
In [2]: article = Article(title='title', content='content')

In [3]: article.save()

In [4]: article.pk
Out[4]: 1

In [5]: comment = Comment()

In [6]: comment.content = 'comment 1'

In [7]: comment.save()

# 에러 발생
IntegrityError: NOT NULL constraint failed: articles_comment.article_id   

In [9]: article
Out[9]: <Article: Article object (1)>

In [10]: comment.article = article

In [11]: comment.save()

In [12]: comment.pk
Out[12]: 1

In [13]: comment.content
Out[13]: 'comment 1'

In [14]: comment.article
Out[14]: <Article: Article object (1)>

In [15]: comment.article_id
Out[15]: 1

In [16]: comment.article.pk
Out[16]: 1

In [17]: comment.article.content
Out[17]: 'content'

In [18]: comment = Comment(content='comment2', article=article)

In [19]: comment.save()

In [20]: comment.pk
Out[20]: 2

In [21]: comment
Out[21]: <Comment: Comment object (2)>

In [22]: comment.article.pk
Out[22]: 1
```

## 관계 모델 참조
- N -> 1 (참조)
    - 댓글이 어떤 게시글에 작성되었는지를 조회
- 1 -> N (역참조)
    - 해당 게시글에 작성된 모든 댓글을 조회

### 역참조
> N:1 관계에서 1에서 N을 참조하거나 조회하는 것
```python
# 모델 인스턴스.related manager(역참조 이름).QuerySet API
article.comment_set.all()
```
- related manager
    - 참조하는 `모델명_set`

```shell
In [3]: article = Article.objects.get(pk=1)

In [4]: article
Out[4]: <Article: Article object (1)>

In [5]: article.comment_set.all()
Out[5]: <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>

In [7]: comments = article.comment_set.all()

In [8]: for comment in comments:
   ...:     print(comment.content)
   ...: 
comment 1
comment2
```

## 댓글 구현
### 댓글 CREATE

### 댓글 READ

### 댓글 DELETE
