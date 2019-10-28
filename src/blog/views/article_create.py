from django.views.generic import CreateView
from ..form import ArticleForm
from ..models import Article


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    model = Article
