from django.urls import path
from .views import product_detail_view, product_create_view, product_delete_view

app_name = 'products'
urlpatterns = [
    path('<int:product_id>', product_detail_view, name='product_details'),
    path('create', product_create_view, name='product_create'),
    path('<int:product_id>/delete', product_delete_view, name='product_delete')
]