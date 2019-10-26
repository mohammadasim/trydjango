from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # The generated Form class will have a form field for every model field specified, in the order specified in the
        # fields attribute.
        fields = ['title', 'body', 'author']
