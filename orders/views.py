from django.shortcuts import render
from .models import Order


def orders_page(request):

    orders = Order.objects.all().order_by('-created_at')

    context = {

        'orders': orders

    }

    return render(
        request,
        'orders/orders.html',
        context
    )