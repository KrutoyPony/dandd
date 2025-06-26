from django.shortcuts import render, get_object_or_404
from main.models import Category, Product
from django.shortcuts import redirect

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {'categories': categories})

def product_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.filter(is_available=True)
    return render(request, 'catalog/product_list.html', {'category': category, 'products': products})

def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, category=category, slug=product_slug)
    return render(request, 'catalog/product_detail.html', {'category': category, 'product': product})

def add_to_cart(request, product_id):
    # Здесь логика корзины
    return redirect(request.META.get('HTTP_REFERER', '/'))