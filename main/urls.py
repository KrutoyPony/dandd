from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),              # Главная страница
    path('catalog/', include('catalog.urls')),   # Каталог
    path('cart/', include('cart.urls')),         # Корзина
    path('contacts/', include('contacts.urls')), # Контакты
]