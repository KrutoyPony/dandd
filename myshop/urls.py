"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView
from django.templatetags.static import static
from django.conf.urls.static import static as static_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),            # ВАЖНО! Это подключает главную страницу /
    path('catalog/', include('catalog.urls')),
    path('contacts/', include('contacts.urls')),
    path('cart/', include('cart.urls')),
    path(r'^favicon\.ico$', RedirectView.as_view(url=static('favicon.ico')))
] + static_urls(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static_urls(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
