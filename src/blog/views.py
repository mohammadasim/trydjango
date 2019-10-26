from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Article
from .form import ArticleForm


def articles_list_view(request):
    articles_list = list(Article.objects.all())
    context = {
        "article_list": articles_list
    }
    return render(request, 'articles/article_list.html', context)


def article_detail_view(request, article_slug):
    obj = Article.objects.get(slug=article_slug)
    context = {
        "object": obj
    }
    return render(request, 'articles/article_detail.html', context)


def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:articles_list'))
    else:
        form = ArticleForm()
    return render(request, 'articles/article_create.html', {'form': form})
