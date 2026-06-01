from django.urls import path

from .views import (
    cart_view,
    add_to_cart,
    remove_from_cart,
    increase_quantity,
    decrease_quantity,
    checkout,
    payment_success
)

app_name = 'cart'

urlpatterns = [

    path(
        '',
        cart_view,
        name='cart'
    ),

    path(
        'add/<int:product_id>/',
        add_to_cart,
        name='add-to-cart'
    ),

    path(
        'remove/<int:cart_id>/',
        remove_from_cart,
        name='remove-from-cart'
    ),

    path(
        'increase/<int:cart_id>/',
        increase_quantity,
        name='increase-quantity'
    ),

    path(
        'decrease/<int:cart_id>/',
        decrease_quantity,
        name='decrease-quantity'
    ),

    path(
        'checkout/',
        checkout,
        name='checkout'
    ),

    path(
        'payment-success/',
        payment_success,
        name='payment-success'
    ),

]