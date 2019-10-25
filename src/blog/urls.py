from django.urls import path
from .views import articles_list_view, article_detail_view

app_name = 'blog'
urlpatterns = [
    path('list/', articles_list_view, name='articles_list'),
    path('<slug:article_slug>/', article_detail_view, name='article_details')
]
