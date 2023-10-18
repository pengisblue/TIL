from rest_framework import serializers
from .models import Article


class ArticleListSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('id', 'title', 'content',)


class ArticleSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
