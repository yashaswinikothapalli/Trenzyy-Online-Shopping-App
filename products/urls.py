from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [

    # HOME PAGE
    path(
        '',
        views.home,
        name='home'
    ),

    # ALL PRODUCTS
    path(
        'products/',
        views.all_products,
        name='products'
    ),

    # PRODUCT DETAILS
    path(
        'product/<int:id>/',
        views.product_details,
        name='product-details'
    ),

    # SEARCH
    path(
        'search/',
        views.search_products,
        name='search-products'
    ),

    # CATEGORY PRODUCTS
    path(
        'category/<int:id>/',
        views.category_products,
        name='category-products'
    ),

]