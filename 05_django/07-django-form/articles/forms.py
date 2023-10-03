from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                # css class 적용
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )
    # model 등록
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)