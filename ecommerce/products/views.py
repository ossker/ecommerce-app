from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product


def index(request):
    categories = Category.objects.all()
    data = {'categories': categories}
    return render(request, 'products/template.html', data)

def category(request, id):
    category = Category.objects.get(pk = id)
    category_products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    data = {'category': category, 'category_products': category_products, 'categories': categories}
    return render(request, 'products/category_product.html', data)

def product(request, id):
    product = Product.objects.get(pk = id)
    categories = Category.objects.all()
    data = {'product': product, 'categories': categories}
    return render(request, 'products/product.html', data)