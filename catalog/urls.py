from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_home, name='catalog_home'),
    path('<slug:section_slug>/', views.catalog_section, name='catalog_section'),
]