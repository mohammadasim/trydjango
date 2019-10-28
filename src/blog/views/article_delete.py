from django.views.generic import DeleteView
from django.urls import reverse_lazy
from ..models import Article


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles_list')
    template_name = 'articles/article_confirm_delete.html'
