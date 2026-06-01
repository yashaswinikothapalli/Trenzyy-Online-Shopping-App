from django.urls import path

from .views import orders_page

app_name = 'orders'

urlpatterns = [

    path(
        '',
        orders_page,
        name='orders'
    ),

]