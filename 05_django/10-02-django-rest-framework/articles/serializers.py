from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    # 필요한 필드만 쓰기 위해서 ArticleSerializer를 재정의
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    # override
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)   # 오버라이드 해서 적용할 수 없음


class ArticleSerializer(serializers.ModelSerializer):
    # 기존에 사용된 CommentSerializer 재사용
    comment_set = CommentSerializer(many=True, read_only=True)
    # article.comment_set.count()
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
