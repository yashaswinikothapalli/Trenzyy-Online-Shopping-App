from .models import Cart


def cart_counter(request):

    cart_items = Cart.objects.all()

    cart_count = sum(
        item.quantity
        for item in cart_items
    )

    return {

        'cart_count': cart_count

    }