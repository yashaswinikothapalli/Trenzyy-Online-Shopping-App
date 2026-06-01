from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('products.urls', 'products'), namespace='products')),

    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),

    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='/login/'),
        name='logout'
    ),
    path(
    'orders/',
    include(('orders.urls', 'orders'),
    namespace='orders')
),
]