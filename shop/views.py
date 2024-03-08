from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Product


# Create your views here.

# FBV - function based views
#
# def product_list(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'shop/shop.html', context)
#

# CBV - class based views

class ProductListView(ListView):
    model = Product
    template_name = 'shop/shop.html'

