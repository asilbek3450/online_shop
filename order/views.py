from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import OrderItem


class OrderItemView(ListView):
    model = OrderItem
    template_name = 'order/cart.html'
    context_object_name = 'order_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = OrderItem.objects.all()
        return context
