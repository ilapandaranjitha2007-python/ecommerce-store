from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),
    path('cart/increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
path('cart/decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
]