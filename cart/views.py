from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.conf import settings

import razorpay

from products.models import Products
from orders.models import Order
from orders.models import OrderItem
from cart.models import Cart
from django.views.decorators.csrf import csrf_exempt


# =========================================
# CART PAGE
# =========================================

def cart_view(request):

    cart_items = Cart.objects.all()

    total_price = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    cart_count = sum(
        item.quantity
        for item in cart_items
    )

    context = {

        'cart_items': cart_items,

        'total_price': total_price,

        'cart_count': cart_count,

    }

    return render(
        request,
        'cart/cart.html',
        context
    )


# =========================================
# ADD TO CART
# =========================================

def add_to_cart(request, product_id):

    product = get_object_or_404(
        Products,
        id=product_id
    )

    cart_item, created = Cart.objects.get_or_create(
        product=product
    )

    if not created:

        cart_item.quantity += 1

        cart_item.save()

    return redirect(
        request.META.get(
            'HTTP_REFERER',
            '/'
        )
    )


# =========================================
# REMOVE FROM CART
# =========================================

def remove_from_cart(request, cart_id):

    item = get_object_or_404(
        Cart,
        id=cart_id
    )

    item.delete()

    return redirect('cart:cart')


# =========================================
# INCREASE QUANTITY
# =========================================

def increase_quantity(request, cart_id):

    item = get_object_or_404(
        Cart,
        id=cart_id
    )

    item.quantity += 1

    item.save()

    return redirect('cart:cart')


# =========================================
# DECREASE QUANTITY
# =========================================

def decrease_quantity(request, cart_id):

    item = get_object_or_404(
        Cart,
        id=cart_id
    )

    if item.quantity > 1:

        item.quantity -= 1

        item.save()

    else:

        item.delete()

    return redirect('cart:cart')


# =========================================
# CHECKOUT PAGE
# =========================================

def checkout(request):

    cart_items = Cart.objects.all()

    total = 0

    for item in cart_items:

        total += item.product.price * item.quantity

    total += 49

    # CREATE RAZORPAY CLIENT

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    payment = client.order.create({

        "amount": int(total * 100),

        "currency": "INR",

        "payment_capture": "1"
    })

    # CREATE ORDER

    order = Order.objects.create(

        full_name="Yashaswini",

        address="Hyderabad",

        phone="9876543210",

        total_price=total,

        razorpay_order_id=payment['id']
    )

    # CREATE ORDER ITEMS

    for item in cart_items:

        OrderItem.objects.create(

            order=order,

            product=item.product,

            quantity=item.quantity,

            price=item.product.price
        )

    context = {

        'payment': payment,

        'order': order,

        'cart_items': cart_items,

        'total': total,

        'razorpay_key': settings.RAZORPAY_KEY_ID,
    }

    return render(
        request,
        'cart/checkout.html',
        context
    )


# =========================================
# PAYMENT SUCCESS
# =========================================

@csrf_exempt
def payment_success(request):

    razorpay_order_id = request.GET.get(
        'razorpay_order_id'
    )

    razorpay_payment_id = request.GET.get(
        'razorpay_payment_id'
    )

    razorpay_signature = request.GET.get(
        'razorpay_signature'
    )

    try:

        order = Order.objects.get(
            razorpay_order_id=razorpay_order_id
        )

        order.razorpay_payment_id = razorpay_payment_id

        order.razorpay_signature = razorpay_signature

        order.is_paid = True

        order.save()

        Cart.objects.all().delete()

    except:
        pass

    return redirect('orders:orders')