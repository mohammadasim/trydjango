from django.views.generic import DetailView
from ..models import Article


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
