from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Category, Product


def product_list(request, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, available=True)
    else:
        category = None
        products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {'category': category, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'products/product_detail.html', {'product': product})