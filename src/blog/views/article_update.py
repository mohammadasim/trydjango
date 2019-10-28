from django.views.generic import UpdateView
from ..models import Article
from ..form import ArticleForm


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_update.html'
