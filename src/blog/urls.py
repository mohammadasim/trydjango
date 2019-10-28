from django.urls import path
from .views.article_list import ArticleListView
from .views.article_detail import ArticleDetail
from .views.article_create import ArticleCreateView
from .views.article_update import ArticleUpdateView
from .views.article_delete import ArticleDeleteView

app_name = 'blog'
urlpatterns = [
    path('list/', ArticleListView.as_view(), name='articles_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('view/<slug:slug>/', ArticleDetail.as_view(), name='article_details'),
    path('update/<slug:slug>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<slug:slug>/', ArticleDeleteView.as_view(), name='article_delete'),

]
