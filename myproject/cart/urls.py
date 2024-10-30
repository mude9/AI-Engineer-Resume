# cart/urls.py
from django.urls import path
from .views import add_to_cart, cart_detail

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('detail/', cart_detail, name='cart_detail'),
]
