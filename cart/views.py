from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.

def add_to_cart(request, product_id):
    # Пока заглушка, просто возвращает назад
    return redirect(request.META.get('HTTP_REFERER', '/'))