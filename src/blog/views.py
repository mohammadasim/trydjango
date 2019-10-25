from django.shortcuts import render
from .models import Article


def articles_list_view(request):
    articles_list = list(Article.objects.all())
    context = {
        "article_list": articles_list
    }
    return render(request, 'articles/articles_list.html', context)


def article_detail_view(request, article_slug):
    print("The article_detail_view method has been called")
    obj = Article.objects.get(slug=article_slug)
    print(obj.get_absolute_url())
    context = {
        "object": obj
    }
    return render(request, 'articles/article_detail.html', context)
