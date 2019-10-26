from django.urls import path
from src.blog.views import car_list, car

app_name = 'blog'
urlpatterns = [
    path('list/', car_list.as_view(), name='articles_list'),
    #path('create/', article_create_view, name='article_create'),
    #path('<slug:article_slug>/', article_detail_view, name='article_details')

]
