from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]