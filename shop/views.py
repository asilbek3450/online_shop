from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shop.models import Product, ProductCategory, ProductImage, ProductReview


# Create your views here.

class HomePageView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['expensive_products'] = Product.objects.all().order_by('-price')[0:8]
        context['recent_products'] = Product.objects.all().order_by('-id')[0:8]
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImage.objects.filter(product=self.object)
        context['related_products'] = Product.objects.filter(category=self.object.category).exclude(id=self.object.id)
        return context

