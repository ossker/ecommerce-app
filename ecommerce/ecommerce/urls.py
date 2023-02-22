from django.contrib import admin
from django.urls import path

from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<id>/', category, name='category'),
    path('product/<id>/', product, name='product'),
]
