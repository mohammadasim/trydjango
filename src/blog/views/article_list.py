from django.views.generic.list import ListView

from ..models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    model = Article
    context_object_name = 'article_list'
    ordering = ['date']
