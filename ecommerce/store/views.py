from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product


def store(request):
    data = {}
    return render(request, 'store/store.html', data)

def cart(request):
    data = {}
    return render(request, 'store/cart.html', data)

def checkout(request):
    data = {}
    return render(request, 'store/checkout.html', data)