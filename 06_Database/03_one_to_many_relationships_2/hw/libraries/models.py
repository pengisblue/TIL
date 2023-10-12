from django.db import models
from django.conf import settings

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)

# 테이블에 저장되는 정보
    # Review 객체의 book 컬럼에 저장되는 값은 book의 pk Integer가 저장
    '''
        libraires_review TABLE
        PK  |   book_id     |    content
        1   |       1       |   1번 책에 대한 리뷰
        2   |       1       |   1번 책에 대한 두번째 리뷰
    '''
# python에서 각 객체로 쓸 수 있는 정보
    '''
        review = Review.objects.get(pk=1)
        review.book = Book.objects.get(pk=review.book_id)
            review.book에 저장한 값 ->
                django가 table에서 book_id에 있는 pk 값으로
                Book Table에서 해당하는 pk의 book 정보를 가져와서
                객체로 만들어서 review.book에 할당 해줌.
            review.book.pk
            review.book.title
            rebiew.book.description
        review.pk
        review.content
        ~~ review.book_id  # 쓸 수는 있음. (django가 만들어 줌) ~~
    '''