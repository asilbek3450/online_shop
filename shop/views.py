from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Product


# Create your views here.

# FBV - function based views
# CBV - class based views

class ProductListView(ListView):
    model = Product
    template_name = 'templates/shop/shop.html'
