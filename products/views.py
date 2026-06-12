from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Products, Category
from cart.models import Cart


# =========================
# CART COUNT
# =========================

def get_cart_count():

    return sum(
        item.quantity
        for item in Cart.objects.all()
    )


# =========================
# HOME PAGE
# =========================

def home(request):

    # ONLY FEW PRODUCTS
    trending_products = Products.objects.all()[:4]

    categories = Category.objects.all()

    context = {

        'trending_products': trending_products,

        'categories': categories,

        'cart_count': get_cart_count()

    }

    return render(
        request,
        'products/home.html',
        context
    )


# =========================
# ALL PRODUCTS
# =========================

def all_products(request):

    products = Products.objects.all()

    categories = Category.objects.all()

    context = {

        'products': products,

        'categories': categories,

        'cart_count': get_cart_count()

    }

    return render(
        request,
        'products/products.html',
        context
    )


# =========================
# PRODUCT DETAILS
# =========================

def product_details(request, id):

    product = get_object_or_404(
        Products,
        id=id
    )

    categories = Category.objects.all()

    context = {

        'product': product,

        'categories': categories,

        'cart_count': get_cart_count()

    }

    return render(
        request,
        'products/product_detail.html',
        context
    )


# =========================
# CATEGORY PRODUCTS
# =========================

def category_products(request, id):

    category = get_object_or_404(
        Category,
        id=id
    )

    products = Products.objects.filter(
        category=category,
         is_available=True
    )

    categories = Category.objects.all()

    context = {

        'category': category,

        'products': products,

        'categories': categories,

        'cart_count': get_cart_count()

    }

    return render(
        request,
        'products/products.html',
        context
    )


# =========================
# SEARCH PRODUCTS
# =========================

def search_products(request):

    query = request.GET.get('q', '')

    products = Products.objects.filter(

        Q(name__icontains=query) |

        Q(desc__icontains=query) |
         Q(category__name__icontains=query)

    )

    categories = Category.objects.all()

    context = {

        'products': products,

        'query': query,

        'categories': categories,

        'cart_count': get_cart_count()

    }

    return render(
        request,
        'products/search.html',
        context
    )